import g4f
import ast
import json
import logging
import random
import string
import time
import nest_asyncio

from flask import request, Response
from typing import List
from ... import debug

from g4f.image import is_allowed_extension, to_image
from g4f.Provider import __providers__
from g4f.Provider.bing.create_images import patch_provider
from .internet import get_search_message

debug.logging = True


class Api:
    def __init__(self,
                 app,
                 env,
                 list_ignored_providers: List[str] = None
                 ) -> None:
        self.app = app
        self.env = env
        self.list_ignored_providers = list_ignored_providers

        nest_asyncio.apply()

        self.routes = {
            '/v1': {
                'function': self.v1,
                'methods': ['GET', 'POST']
            },
            '/v1/providers': {
                'function': self.v1_providers,
                'methods': ['GET', 'POST']
            },
            '/v1/providers/<provider_name>': {
                'function': self.v1_providers_info,
                'methods': ['GET', 'POST']
            },
            '/v1/models': {
                'function': self.v1_models,
                'methods': ['GET', 'POST']
            },
            '/v1/models/<model_name>': {
                'function': self.v1_model_info,
                'methods': ['GET', 'POST']
            },
            '/v1/chat/completions': {
                'function': self.v1_chat_completions,
                'methods': ['GET', 'POST']
            },
            '/v1/completions': {
                'function': self.v1_completions,
                'methods': ['GET', 'POST']
            },
        }

    def v1(self):
        return self.responseJson({
            "error": {
                "message": "Go to /v1/chat/completions or /v1/models.",
                "type": "invalid_request_error",
                "param": "null",
                "code": "null",
            }
        }, status=404)

    def v1_models(self):
        model_list = []
        for model in g4f.Model.__all__():
            model_info = (g4f.ModelUtils.convert[model])
            model_list.append({
                'id': model,
                'object': 'model',
                'created': 0,
                'owned_by': model_info.base_provider}
            )
        return self.responseJson({
            'object': 'list',
            'data': model_list})

    def v1_model_info(self, model_name: str):
        try:
            model_info = (g4f.ModelUtils.convert[model_name])
            return self.responseJson({
                'id': model_name,
                'object': 'model',
                'created': 0,
                'owned_by': model_info.base_provider
            })
        except Exception:
            return self.responseJson({
                "error": {
                    "message": "The model does not exist.",
                    "type": "invalid_request_error",
                    "param": "null",
                    "code": "null",
                }
            }, status=500)

    def v1_providers(self):
        provider_list = []
        for provider in __providers__:
            provider_list.append({
                'id': provider.__name__,
                'object': 'provider',
                'url': provider.url,
                'working': provider.working,
                'supports_message_history': provider.supports_message_history,
                'supports_gpt_4': provider.supports_gpt_4,
                'supports_gpt_35_turbo': provider.supports_gpt_35_turbo,
                'supports_stream': provider.supports_stream,
            })
        return self.responseJson({
            'object': 'list',
            'data': provider_list})
    
    def v1_providers_info(self, provider_name: str):
        try:
            provider = (g4f.ProviderUtils.convert[provider_name])
            return self.responseJson({
                'id': provider.__name__,
                'object': 'provider',
                'url': provider.url,
                'working': provider.working,
                'supports_message_history': provider.supports_message_history,
                'supports_gpt_4': provider.supports_gpt_4,
                'supports_gpt_35_turbo': provider.supports_gpt_35_turbo,
                'supports_stream': provider.supports_stream,
            })
        except Exception:
            return self.responseJson({
                "error": {
                    "message": "The provider does not exist.",
                    "type": "invalid_request_error",
                    "param": "null",
                    "code": "null",
                }
            }, status=500)

    def v1_chat_completions(self):
        if request.method == 'GET':
            return self.responseJson({
                "error": {
                    "message":
                    "You must use POST to access this endpoint.",
                    "type": "invalid_request_error",
                    "param": "null",
                    "code": "null",
                }
            }, status=501)
        kwargs = {}
        item = request.get_json()
        item_data = {
            'model': 'gpt-3.5-turbo',
            'stream': False,
        }
        item_data.update({
            key.decode('utf-8')
            if isinstance(key, bytes) else key: str(value)
            for key, value in (item or {}).items()
        })
        if isinstance(item_data.get('messages'), str):
            item_data['messages'] = ast.literal_eval(
                item_data.get('messages'))

        if 'image' in request.files:
            file = request.files['image']
            if file.filename != '' and is_allowed_extension(file.filename):
                kwargs['image'] = to_image(file.stream)

        if item_data.get('image'):
            kwargs['image'] = to_image(item_data.get('image'))

        model = item_data.get('model')
        stream = True if item_data.get("stream") == "True" else False
        messages = item_data.get('messages')
        envprovider = self.env.get('provider') if self.env.get(
            'provider') else item_data.get('provider', '')
        provider = envprovider.replace('g4f.Provider.', '')
        provider = provider if provider and provider != "Auto" else None
        if provider == 'OpenaiChat':
            kwargs['auto_continue'] = True
        if item_data.get('web_search') or self.env.get('web_search'):
            if provider == "Bing":
                kwargs['web_search'] = True
            else:
                messages[-1]["content"] = get_search_message(
                    messages[-1]["content"])
        patch = patch_provider if item_data.get('patch_provider') else None

        try:
            response = g4f.ChatCompletion.create(
                model=model,
                stream=stream,
                messages=messages,
                provider=provider,
                proxy=self.env.get('proxy', None),
                socks5=self.env.get('socks5', None),
                time=self.env.get('timeout', 120),
                patch_provider=patch,
                ignored=self.list_ignored_providers,
                **kwargs
            )
        except Exception as e:
            logging.exception(e)
            return self.responseJson({
                "error": {
                    "message":
                    f"An error occurred while generating the response:\n{e}"
                },
                "model": model,
                "provider": g4f.get_last_provider(True)
            }, status=500)

        completion_id = ''.join(random.choices(
            string.ascii_letters + string.digits, k=28))
        completion_timestamp = int(time.time())

        if not stream:
            json_data = {
                'id': f'chatcmpl-{completion_id}',
                'object': 'chat.completion',
                'created': completion_timestamp,
                'model': model,
                'provider': g4f.get_last_provider(True),
                'choices': [
                    {
                        'index': 0,
                        'message': {
                            'role': 'assistant',
                            'content': response,
                        },
                        'finish_reason': 'stop',
                    }
                ],
                'usage': {
                    'prompt_tokens': 0,
                    'completion_tokens': 0,
                    'total_tokens': 0,
                },
            }

            return self.responseJson(
                json_data,
                content_type="application/json"
            )

        def streaming():
            try:
                for chunk in response:
                    completion_data = {
                        'id': f'chatcmpl-{completion_id}',
                        'object': 'chat.completion.chunk',
                        'created': completion_timestamp,
                        'model': model,
                        'provider': g4f.get_last_provider(True),
                        'choices': [
                            {
                                'index': 0,
                                'delta': {
                                    'content': chunk,
                                },
                                'finish_reason': None,
                            }
                        ],
                    }
                    yield f'data: {json.dumps(completion_data)}\n'

                end_completion_data = {
                    'id': f'chatcmpl-{completion_id}',
                    'object': 'chat.completion.chunk',
                    'created': completion_timestamp,
                    'model': model,
                    'provider': g4f.get_last_provider(True),
                    'choices': [
                        {
                            'index': 0,
                            'delta': {},
                            'finish_reason': 'stop',
                        }
                    ],
                }
                yield f'data: {json.dumps(end_completion_data)}\n'

            except GeneratorExit:
                pass
            except Exception as e:
                logging.exception(e)
                content = json.dumps({
                    "error": {
                        "message": f"An error occurred while generating the response:\n{e}"
                    },
                    "model": model,
                    "provider": g4f.get_last_provider(True),
                })
                yield f'data: {content}'

        return Response(
            streaming(),
            content_type='text/event-stream'
        )

    def v1_completions(self):
        return self.responseJson({'info': 'Not working yet.'})

    def responseJson(self, response,
                     content_type="application/json", status=200):
        return Response(
            json.dumps(response, indent=4),
            content_type=content_type,
            status=status)
