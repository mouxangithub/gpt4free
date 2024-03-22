![248433934-7886223b-c1d1-4260-82aa-da5741f303bb](https://github.com/xtekky/gpt4free/assets/98614666/ea012c87-76e0-496a-8ac4-e2de090cc6c9)

<div id="top"></div>

> [!Note]
<sup><strong>Lastet version:</strong></sup> [![Docker version](https://img.shields.io/docker/v/mouxan/g4f?label=docker&color=blue)](https://hub.docker.com/r/mouxan/g4f)  
>

## 🛠️ 部署方法

### 环境变量说明

```sh
# PROXY和SOCKS5为代理地址
# TIMEOUT为请求接口超时时间，单位s
# web_search是否开启联网搜索
# provider Api接口供应商
```

### Railway部署

- 1.[注册Railway](https://railway.app?referralCode=bbE8bz)

- 2.点击一键部署：[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/zIYnPJ?referralCode=bbE8bz)

- 3.点击部署的服务，进入Settings->Networking->Generate Domain（生成随机域名）/Custom Domain（绑定自定义自己的域名），然后就可以通过这个域名进行原神启动！

Tips: 如果你不是新用户，五刀用完了，别慌，点击右上角头像进入settings->General->拉到最下面Delete Account，对，这是注销解绑，然后再重新用github登录绑定，然后你会发现，又有五刀了

### docker部署

```sh
docker pull mouxan/g4f
docker run -d --restart always --name gpt4free \
            -p 8080:80 \
            -e PROXY=http://127.0.0.1:3333 \
            -e TIMEOUT=60 \
            -e web_search=true \
            -e provider='Bing' \
            mouxan/g4f
```

### docker-compose.yml

```sh
version: '3'
services:
  gpt4free:
    container_name: gpt4free
    image: mouxan/g4f:latest
    restart: always
    environment:
      PROXY: http://127.0.0.1:3333
      TIMEOUT: 60
      web_search: true
      provider: 'Bing'
    ports:
      - 8080:80
```

### git本地部署

```sh
git clone https://github.com/mouxangithub/gpt4free.git
cd gpt4free
pip install -r requirements.txt
python -m cli all
```

## 💡 使用方法

### Gui访问

```sh
http://127.0.0.1/chat/
```

### Api请求

- completions接口

```shell
curl --location 'http://127.0.0.1/v1/chat/completions' \
--header 'Content-Type: application/json' \
--data '{
  "web_search": true,
  "provider": "Bing",
  "model": "gpt-4",
  "messages": [{"role": "user", "content": "hi"}]
}'
# web_search为是否开启联网搜索，目前gpt4模型兼容性好一些，部分gpt3.5好像无法进行联网搜索
# provider API供应商名称，可请求查看下方/v1/providers查看有哪些供应商名称，可指定working为true的供应商，亦可直接环境变量设置，不传则默认随机请求，如果a供应商接口无法请求则会继续b供应商然后继续往下，但如果传了该参数则无法继续请求
```

- providers接口，查看供应商列表

```shell
curl --location 'http://127.0.0.1/v1/providers/<provider_name>'
```

- models接口，查看api支持的模型，以及模型所对应的供应商

```shell
curl --location 'http://127.0.0.1/v1/models/<model_name>'
```

## 🚀 API服务商和模型

### GPT-4

| Website | Provider | GPT-3.5 | GPT-4 | Stream | Status | Auth |
| ------  | -------  | ------- | ----- | ------ | ------ | ---- |
| [bing.com](https://bing.com/chat) | `g4f.Provider.Bing` | ❌ | ✔️ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [chat.geekgpt.org](https://chat.geekgpt.org) | `g4f.Provider.GeekGpt` | ✔️ | ✔️ | ✔️ | ![Unknown](https://img.shields.io/badge/Unknown-grey) | ❌ |
| [gptchatly.com](https://gptchatly.com) | `g4f.Provider.GptChatly` | ✔️ | ✔️ | ❌ | ![Unknown](https://img.shields.io/badge/Unknown-grey) | ❌ |
| [liaobots.site](https://liaobots.site) | `g4f.Provider.Liaobots` | ✔️ | ✔️ | ✔️ | ![Unknown](https://img.shields.io/badge/Unknown-grey) | ❌ |
| [www.phind.com](https://www.phind.com) | `g4f.Provider.Phind` | ❌ | ✔️ | ✔️ | ![Unknown](https://img.shields.io/badge/Unknown-grey) | ❌ |
| [raycast.com](https://raycast.com) | `g4f.Provider.Raycast` | ✔️ | ✔️ | ✔️ | ![Unknown](https://img.shields.io/badge/Unknown-grey) | ✔️ |

### GPT-3.5

| Website | Provider | GPT-3.5 | GPT-4 | Stream | Status | Auth |
| ------  | -------  | ------- | ----- | ------ | ------ | ---- |
| [www.aitianhu.com](https://www.aitianhu.com) | `g4f.Provider.AItianhu` | ✔️ | ❌ | ✔️ | ![Unknown](https://img.shields.io/badge/Unknown-grey) | ❌ |
| [chat3.aiyunos.top](https://chat3.aiyunos.top/) | `g4f.Provider.AItianhuSpace` | ✔️ | ❌ | ✔️ | ![Unknown](https://img.shields.io/badge/Unknown-grey) | ❌ |
| [e.aiask.me](https://e.aiask.me) | `g4f.Provider.AiAsk` | ✔️ | ❌ | ✔️ | ![Unknown](https://img.shields.io/badge/Unknown-grey) | ❌ |
| [chat-gpt.org](https://chat-gpt.org/chat) | `g4f.Provider.Aichat` | ✔️ | ❌ | ❌ | ![Unknown](https://img.shields.io/badge/Unknown-grey) | ❌ |
| [www.chatbase.co](https://www.chatbase.co) | `g4f.Provider.ChatBase` | ✔️ | ❌ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [chatforai.store](https://chatforai.store) | `g4f.Provider.ChatForAi` | ✔️ | ❌ | ✔️ | ![Unknown](https://img.shields.io/badge/Unknown-grey) | ❌ |
| [chatgpt.ai](https://chatgpt.ai) | `g4f.Provider.ChatgptAi` | ✔️ | ❌ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [chatgptx.de](https://chatgptx.de) | `g4f.Provider.ChatgptX` | ✔️ | ❌ | ✔️ | ![Unknown](https://img.shields.io/badge/Unknown-grey) | ❌ |
| [chat-shared2.zhile.io](https://chat-shared2.zhile.io) | `g4f.Provider.FakeGpt` | ✔️ | ❌ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [freegpts1.aifree.site](https://freegpts1.aifree.site/) | `g4f.Provider.FreeGpt` | ✔️ | ❌ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [gptalk.net](https://gptalk.net) | `g4f.Provider.GPTalk` | ✔️ | ❌ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [ai18.gptforlove.com](https://ai18.gptforlove.com) | `g4f.Provider.GptForLove` | ✔️ | ❌ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [gptgo.ai](https://gptgo.ai) | `g4f.Provider.GptGo` | ✔️ | ❌ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [hashnode.com](https://hashnode.com) | `g4f.Provider.Hashnode` | ✔️ | ❌ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [app.myshell.ai](https://app.myshell.ai/chat) | `g4f.Provider.MyShell` | ✔️ | ❌ | ✔️ | ![Unknown](https://img.shields.io/badge/Unknown-grey) | ❌ |
| [noowai.com](https://noowai.com) | `g4f.Provider.NoowAi` | ✔️ | ❌ | ✔️ | ![Unknown](https://img.shields.io/badge/Unknown-grey) | ❌ |
| [chat.openai.com](https://chat.openai.com) | `g4f.Provider.OpenaiChat` | ✔️ | ❌ | ✔️ | ![Unknown](https://img.shields.io/badge/Unknown-grey) | ✔️ |
| [theb.ai](https://theb.ai) | `g4f.Provider.Theb` | ✔️ | ❌ | ✔️ | ![Unknown](https://img.shields.io/badge/Unknown-grey) | ✔️ |
| [sdk.vercel.ai](https://sdk.vercel.ai) | `g4f.Provider.Vercel` | ✔️ | ❌ | ✔️ | ![Unknown](https://img.shields.io/badge/Unknown-grey) | ❌ |
| [you.com](https://you.com) | `g4f.Provider.You` | ✔️ | ❌ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [chat9.yqcloud.top](https://chat9.yqcloud.top/) | `g4f.Provider.Yqcloud` | ✔️ | ❌ | ✔️ | ![Unknown](https://img.shields.io/badge/Unknown-grey) | ❌ |
| [chat.acytoo.com](https://chat.acytoo.com) | `g4f.Provider.Acytoo` | ✔️ | ❌ | ✔️ | ![Inactive](https://img.shields.io/badge/Inactive-red) | ❌ |
| [aibn.cc](https://aibn.cc) | `g4f.Provider.Aibn` | ✔️ | ❌ | ✔️ | ![Inactive](https://img.shields.io/badge/Inactive-red) | ❌ |
| [ai.ls](https://ai.ls) | `g4f.Provider.Ails` | ✔️ | ❌ | ✔️ | ![Inactive](https://img.shields.io/badge/Inactive-red) | ❌ |
| [chatgpt4online.org](https://chatgpt4online.org) | `g4f.Provider.Chatgpt4Online` | ✔️ | ❌ | ✔️ | ![Inactive](https://img.shields.io/badge/Inactive-red) | ❌ |
| [chat.chatgptdemo.net](https://chat.chatgptdemo.net) | `g4f.Provider.ChatgptDemo` | ✔️ | ❌ | ✔️ | ![Inactive](https://img.shields.io/badge/Inactive-red) | ❌ |
| [chatgptduo.com](https://chatgptduo.com) | `g4f.Provider.ChatgptDuo` | ✔️ | ❌ | ❌ | ![Inactive](https://img.shields.io/badge/Inactive-red) | ❌ |
| [chatgptfree.ai](https://chatgptfree.ai) | `g4f.Provider.ChatgptFree` | ✔️ | ❌ | ❌ | ![Inactive](https://img.shields.io/badge/Inactive-red) | ❌ |
| [chatgptlogin.ai](https://chatgptlogin.ai) | `g4f.Provider.ChatgptLogin` | ✔️ | ❌ | ✔️ | ![Inactive](https://img.shields.io/badge/Inactive-red) | ❌ |
| [cromicle.top](https://cromicle.top) | `g4f.Provider.Cromicle` | ✔️ | ❌ | ✔️ | ![Inactive](https://img.shields.io/badge/Inactive-red) | ❌ |
| [gptgod.site](https://gptgod.site) | `g4f.Provider.GptGod` | ✔️ | ❌ | ✔️ | ![Inactive](https://img.shields.io/badge/Inactive-red) | ❌ |
| [opchatgpts.net](https://opchatgpts.net) | `g4f.Provider.Opchatgpts` | ✔️ | ❌ | ✔️ | ![Inactive](https://img.shields.io/badge/Inactive-red) | ❌ |
| [chat.ylokh.xyz](https://chat.ylokh.xyz) | `g4f.Provider.Ylokh` | ✔️ | ❌ | ✔️ | ![Inactive](https://img.shields.io/badge/Inactive-red) | ❌ |

### 其他

| Website | Provider | GPT-3.5 | GPT-4 | Stream | Status | Auth |
| ------  | -------  | ------- | ----- | ------ | ------ | ---- |
| [bard.google.com](https://bard.google.com) | `g4f.Provider.Bard` | ❌ | ❌ | ❌ | ![Unknown](https://img.shields.io/badge/Unknown-grey) | ✔️ |
| [deepinfra.com](https://deepinfra.com) | `g4f.Provider.DeepInfra` | ❌ | ❌ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [huggingface.co](https://huggingface.co/chat) | `g4f.Provider.HuggingChat` | ❌ | ❌ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ✔️ |
| [www.llama2.ai](https://www.llama2.ai) | `g4f.Provider.Llama2` | ❌ | ❌ | ✔️ | ![Unknown](https://img.shields.io/badge/Unknown-grey) | ❌ |
| [open-assistant.io](https://open-assistant.io/chat) | `g4f.Provider.OpenAssistant` | ❌ | ❌ | ✔️ | ![Inactive](https://img.shields.io/badge/Inactive-red) | ✔️ |

### 其他模型

| Model                                   | Base Provider | Provider            | Website                                     |
| --------------------------------------- | ------------- | ------------------- | ------------------------------------------- |
| palm                                    | Google        | g4f.Provider.Bard   | [bard.google.com](https://bard.google.com/) |
| h2ogpt-gm-oasst1-en-2048-falcon-7b-v3   | Hugging Face  | g4f.Provider.H2o    | [www.h2o.ai](https://www.h2o.ai/)           |
| h2ogpt-gm-oasst1-en-2048-falcon-40b-v1  | Hugging Face  | g4f.Provider.H2o    | [www.h2o.ai](https://www.h2o.ai/)           |
| h2ogpt-gm-oasst1-en-2048-open-llama-13b | Hugging Face  | g4f.Provider.H2o    | [www.h2o.ai](https://www.h2o.ai/)           |
| claude-instant-v1                       | Anthropic     | g4f.Provider.Vercel | [sdk.vercel.ai](https://sdk.vercel.ai/)     |
| claude-v1                               | Anthropic     | g4f.Provider.Vercel | [sdk.vercel.ai](https://sdk.vercel.ai/)     |
| claude-v2                               | Anthropic     | g4f.Provider.Vercel | [sdk.vercel.ai](https://sdk.vercel.ai/)     |
| command-light-nightly                   | Cohere        | g4f.Provider.Vercel | [sdk.vercel.ai](https://sdk.vercel.ai/)     |
| command-nightly                         | Cohere        | g4f.Provider.Vercel | [sdk.vercel.ai](https://sdk.vercel.ai/)     |
| gpt-neox-20b                            | Hugging Face  | g4f.Provider.Vercel | [sdk.vercel.ai](https://sdk.vercel.ai/)     |
| oasst-sft-1-pythia-12b                  | Hugging Face  | g4f.Provider.Vercel | [sdk.vercel.ai](https://sdk.vercel.ai/)     |
| oasst-sft-4-pythia-12b-epoch-3.5        | Hugging Face  | g4f.Provider.Vercel | [sdk.vercel.ai](https://sdk.vercel.ai/)     |
| santacoder                              | Hugging Face  | g4f.Provider.Vercel | [sdk.vercel.ai](https://sdk.vercel.ai/)     |
| bloom                                   | Hugging Face  | g4f.Provider.Vercel | [sdk.vercel.ai](https://sdk.vercel.ai/)     |
| flan-t5-xxl                             | Hugging Face  | g4f.Provider.Vercel | [sdk.vercel.ai](https://sdk.vercel.ai/)     |
| code-davinci-002                        | OpenAI        | g4f.Provider.Vercel | [sdk.vercel.ai](https://sdk.vercel.ai/)     |
| gpt-3.5-turbo-16k                       | OpenAI        | g4f.Provider.Vercel | [sdk.vercel.ai](https://sdk.vercel.ai/)     |
| gpt-3.5-turbo-16k-0613                  | OpenAI        | g4f.Provider.Vercel | [sdk.vercel.ai](https://sdk.vercel.ai/)     |
| gpt-4-0613                              | OpenAI        | g4f.Provider.Vercel | [sdk.vercel.ai](https://sdk.vercel.ai/)     |
| text-ada-001                            | OpenAI        | g4f.Provider.Vercel | [sdk.vercel.ai](https://sdk.vercel.ai/)     |
| text-babbage-001                        | OpenAI        | g4f.Provider.Vercel | [sdk.vercel.ai](https://sdk.vercel.ai/)     |
| text-curie-001                          | OpenAI        | g4f.Provider.Vercel | [sdk.vercel.ai](https://sdk.vercel.ai/)     |
| text-davinci-002                        | OpenAI        | g4f.Provider.Vercel | [sdk.vercel.ai](https://sdk.vercel.ai/)     |
| text-davinci-003                        | OpenAI        | g4f.Provider.Vercel | [sdk.vercel.ai](https://sdk.vercel.ai/)     |
| llama13b-v2-chat                        | Replicate     | g4f.Provider.Vercel | [sdk.vercel.ai](https://sdk.vercel.ai/)     |
| llama7b-v2-chat                         | Replicate     | g4f.Provider.Vercel | [sdk.vercel.ai](https://sdk.vercel.ai/)     |



<details>
<summary>
     官方原文档，尊重敬重各位大佬gpt4free的提供开源者，如有侵权行为，请联系我关闭下架，官方原文档我就合起来了，有需要看的自行咱开或者前往官方github：[gpt4free](https://github.com/xtekky/gpt4free) 浏览
</summary>

<div id="top"></div>

Written by [@xtekky](https://github.com/hlohaus) & maintained by [@hlohaus](https://github.com/hlohaus)

<div id="top"></div>

> By using this repository or any code related to it, you agree to the [legal notice](LEGAL_NOTICE.md). The author is **not responsible for the usage of this repository nor endorses it**, nor is the author responsible for any copies, forks, re-uploads made by other users, or anything else related to GPT4Free. This is the author's only account and repository. To prevent impersonation or irresponsible actions, please comply with the GNU GPL license this Repository uses.  

> [!Warning]
*"gpt4free"* serves as a **PoC** (proof of concept), demonstrating the development of an API package with multi-provider requests, with features like timeouts, load balance and flow control.

> [!Note]
<sup><strong>Lastet version:</strong></sup> [![PyPI version](https://img.shields.io/pypi/v/g4f?color=blue)](https://pypi.org/project/g4f) [![Docker version](https://img.shields.io/docker/v/hlohaus789/g4f?label=docker&color=blue)](https://hub.docker.com/r/hlohaus789/g4f)  
> <sup><strong>Stats:</strong></sup>  [![Downloads](https://static.pepy.tech/badge/g4f)](https://pepy.tech/project/g4f) [![Downloads](https://static.pepy.tech/badge/g4f/month)](https://pepy.tech/project/g4f)

```sh
pip install -U g4f
```
```sh
docker pull hlohaus789/g4f
```

## 🆕 What's New

- Check out a more in depth local inference @ https://github.com/gpt4free/gpt4local
- Join our Telegram Channel: [t.me/g4f_channel](https://telegram.me/g4f_channel)
- Join our Discord Group: [discord.gg/XfybzPXPH5](https://discord.gg/XfybzPXPH5)
- `g4f` now supports 100% local inference: [local-docs](https://g4f.mintlify.app/docs/core/usage/local)

## 🔻 Site Takedown
Is your site on this repository and you want to take it down? Send an email to takedown@g4f.ai with proof it is yours and it will be removed as fast as possible. To prevent reproduction please secure your API ;)

## 🚀  Feedback and Todo
You can always leave some feedback here: https://forms.gle/FeWV9RLEedfdkmFN6

As per the survey, here is a list of improvements to come
- [x] Update the repository to include the new openai library syntax (ex: `Openai()` class) | completed, use `g4f.client.Client`
- [ ] Golang implementation
- [ ] 🚧 Improve Documentation (in /docs & Guides, Howtos, & Do video tutorials)
- [x] Improve the provider status list & updates
- [ ] Tutorials on how to reverse sites to write your own wrapper (PoC only ofc)
- [x] Improve the Bing wrapper. (Wait and Retry or reuse conversation)
- [ ] Write a standard provider performance test to improve the stability
- [ ] Potential support and development of local models
- [ ] 🚧 Improve compatibility and error handling

## 📚 Table of Contents

- [🆕 What's New](#-whats-new)
- [📚 Table of Contents](#-table-of-contents)
- [🛠️ Getting Started](#-getting-started)
    + [Docker container](#docker-container)
      - [Quick start](#quick-start)
    + [Use python](#use-python)
      - [Prerequisites](#prerequisites)
      - [Install using PyPI package:](#install-using-pypi-package)
      - [Install from source:](#install-from-source)
      - [Install using Docker:](#install-using-docker)
- [💡 Usage](#-usage)
  * [Text Generation](#text-generation)
  * [Image Generation](#image-generation)
  * [Web UI](#web-ui)
  * [Interference API](#interference-api)
  * [Configuration](#configuration)
- [🚀 Providers and Models](#-providers-and-models)
  * [GPT-4](#gpt-4)
  * [GPT-3.5](#gpt-35)
  * [Other](#other)
  * [Models](#models)
- [🔗 Related GPT4Free Projects](#-related-gpt4free-projects)
- [🤝 Contribute](#-contribute)
    + [How do i create a new Provider?](#guide-how-do-i-create-a-new-provider)
    + [How can AI help me with writing code?](#guide-how-can-ai-help-me-with-writing-code)
- [🙌 Contributors](#-contributors)
- [©️ Copyright](#-copyright)
- [⭐ Star History](#-star-history)
- [📄 License](#-license)

## 🛠️ Getting Started

#### Docker container

##### Quick start:

1. [Download and install Docker](https://docs.docker.com/get-docker/)
2. Pull latest image and run the container:

```sh
docker pull hlohaus789/g4f
docker run -p 8080:8080 -p 1337:1337 -p 7900:7900 --shm-size="2g" hlohaus789/g4f:latest
```
3. Open the included client on: [http://localhost:8080/chat/](http://localhost:8080/chat/)
or set the API base in your client to: [http://localhost:1337/v1](http://localhost:1337/v1)
4. (Optional) If you need to log in to a provider, you can view the desktop from the container here: http://localhost:7900/?autoconnect=1&resize=scale&password=secret.

##### Use your smartphone:

Run the Web UI on Your Smartphone:
- [/docs/guides/phone](/docs/guides/phone.md)

#### Use python

##### Prerequisites:

1. [Download and install Python](https://www.python.org/downloads/) (Version 3.10+ is recommended).
2. [Install Google Chrome](https://www.google.com/chrome/) for providers with webdriver

##### Install using PyPI package:

```
pip install -U g4f[all]
```

How do I install only parts or do disable parts?
Use partial requirements: [/docs/requirements](/docs/requirements.md)

##### Install from source:

How do I load the project using git and installing the project requirements?
Read this tutorial and follow it step by step: [/docs/git](/docs/git.md)


##### Install using Docker:

How do I build and run composer image from source?
Use docker-compose: [/docs/docker](/docs/docker.md)


## 💡 Usage

#### Text Generation

```python
from g4f.client import Client

client = Client()
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello"}],
    ...
)
print(response.choices[0].message.content)
```

```
Hello! How can I assist you today?
```

#### Image Generation

```python
from g4f.client import Client

client = Client()
response = client.images.generate(
  model="gemini",
  prompt="a white siamese cat",
  ...
)
image_url = response.data[0].url
```


[![Image with cat](/docs/cat.jpeg)](/docs/client.md)

**Full Documentation for Python API**

- New Client API like the OpenAI Python library: [/docs/client](/docs/client.md)
- Legacy API with python modules: [/docs/legacy](/docs/legacy.md)

### Webview GUI

Open the GUI in a window of your OS. Runs on a local/static/ssl server with a js api. Supports login into the OpenAI Chat, Image Upload and streamed Text Generation.

Supports all platforms, but only Linux tested.

1. Install all requirements with:

```bash
pip install g4f[webview]
```

2. Follow the OS specific steps here:
 [pywebview installation](https://pywebview.flowrl.com/guide/installation.html#dependencies)

3. Run the app with:

```python
from g4f.gui.webview import run_webview
run_webview(debug=True)
```
or execute the following command:
```bash
python -m g4f.gui.webview -debug
```

#### Webserver

To start the web interface, type the following codes in python:

```python
from g4f.gui import run_gui
run_gui()
```
or execute the following command:
```bash
python -m g4f.cli gui -port 8080 -debug
```

### Interference API

You can use the Interference API to serve other OpenAI integrations with G4F.

See: [/docs/interference](/docs/interference.md)

### Configuration

##### Cookies / Access Token

For generating images with Bing and for the OpenAI Chat  you need cookies or a token from your browser session. From Bing you need the "_U" cookie and from OpenAI you need the "access_token". You can pass the cookies / the access token in the create function or you use the `set_cookies` setter before you run G4F:

```python
from g4f.cookies import set_cookies

set_cookies(".bing.com", {
  "_U": "cookie value"
})
set_cookies("chat.openai.com", {
  "access_token": "token value"
})
set_cookies(".google.com", {
  "__Secure-1PSID": "cookie value"
})

...
```

Alternatively, G4F reads the cookies with `browser_cookie3` from your browser
or it starts a browser instance with selenium `webdriver` for logging in.

##### Using Proxy

If you want to hide or change your IP address for the providers, you can set a proxy globally via an environment variable:

- On macOS and Linux:
```bash
export G4F_PROXY="http://host:port"
```

- On Windows:
```bash
set G4F_PROXY=http://host:port
```

## 🚀 Providers and Models

### GPT-4

| Website | Provider | GPT-3.5 | GPT-4 | Stream | Status | Auth |
| ------  | -------  | ------- | ----- | ------ | ------ | ---- |
| [bing.com](https://bing.com/chat) | `g4f.Provider.Bing` | ❌ | ✔️ | ✔️ | ![Unknown](https://img.shields.io/badge/Unknown-grey) | ❌ |
| [chatgpt.ai](https://chatgpt.ai) | `g4f.Provider.ChatgptAi` | ❌ | ✔️ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [liaobots.site](https://liaobots.site) | `g4f.Provider.Liaobots` | ✔️ | ✔️ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [chat.openai.com](https://chat.openai.com) | `g4f.Provider.OpenaiChat` | ✔️ | ❌ | ✔️ | ![Unknown](https://img.shields.io/badge/Unknown-grey) | ✔️ |
| [raycast.com](https://raycast.com) | `g4f.Provider.Raycast` | ✔️ | ✔️ | ✔️ | ![Unknown](https://img.shields.io/badge/Unknown-grey) | ✔️ |
| [beta.theb.ai](https://beta.theb.ai) | `g4f.Provider.Theb` | ✔️ | ✔️ | ✔️ | ![Unknown](https://img.shields.io/badge/Unknown-grey) | ❌ |
| [you.com](https://you.com) | `g4f.Provider.You` | ✔️ | ✔️ | ✔️ | ![Unknown](https://img.shields.io/badge/Unknown-grey) | ❌ |

### GPT-3.5

| Website | Provider | GPT-3.5 | GPT-4 | Stream | Status | Auth |
| ------  | -------  | ------- | ----- | ------ | ------ | ---- |
| [chat3.aiyunos.top](https://chat3.aiyunos.top/) | `g4f.Provider.AItianhuSpace` | ✔️ | ❌ | ✔️ | ![Unknown](https://img.shields.io/badge/Unknown-grey) | ❌ |
| [chatforai.store](https://chatforai.store) | `g4f.Provider.ChatForAi` | ✔️ | ❌ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [chatgpt4online.org](https://chatgpt4online.org) | `g4f.Provider.Chatgpt4Online` | ✔️ | ❌ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [chatgpt-free.cc](https://www.chatgpt-free.cc) | `g4f.Provider.ChatgptNext` | ✔️ | ❌ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [chatgptx.de](https://chatgptx.de) | `g4f.Provider.ChatgptX` | ✔️ | ❌ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [flowgpt.com](https://flowgpt.com/chat) | `g4f.Provider.FlowGpt` | ✔️ | ❌ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [freegptsnav.aifree.site](https://freegptsnav.aifree.site) | `g4f.Provider.FreeGpt` | ✔️ | ❌ | ✔️ | ![Unknown](https://img.shields.io/badge/Unknown-grey) | ❌ |
| [gpttalk.ru](https://gpttalk.ru) | `g4f.Provider.GptTalkRu` | ✔️ | ❌ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [koala.sh](https://koala.sh) | `g4f.Provider.Koala` | ✔️ | ❌ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [app.myshell.ai](https://app.myshell.ai/chat) | `g4f.Provider.MyShell` | ✔️ | ❌ | ✔️ | ![Unknown](https://img.shields.io/badge/Unknown-grey) | ❌ |
| [perplexity.ai](https://www.perplexity.ai) | `g4f.Provider.PerplexityAi` | ✔️ | ❌ | ✔️ | ![Unknown](https://img.shields.io/badge/Unknown-grey) | ❌ |
| [poe.com](https://poe.com) | `g4f.Provider.Poe` | ✔️ | ❌ | ✔️ | ![Unknown](https://img.shields.io/badge/Unknown-grey) | ✔️ |
| [talkai.info](https://talkai.info) | `g4f.Provider.TalkAi` | ✔️ | ❌ | ✔️ | ![Unknown](https://img.shields.io/badge/Unknown-grey) | ❌ |
| [chat.vercel.ai](https://chat.vercel.ai) | `g4f.Provider.Vercel` | ✔️ | ❌ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [aitianhu.com](https://www.aitianhu.com) | `g4f.Provider.AItianhu` | ✔️ | ❌ | ✔️ | ![Inactive](https://img.shields.io/badge/Inactive-red) | ❌ |
| [chatgpt.bestim.org](https://chatgpt.bestim.org) | `g4f.Provider.Bestim` | ✔️ | ❌ | ✔️ | ![Inactive](https://img.shields.io/badge/Inactive-red) | ❌ |
| [chatbase.co](https://www.chatbase.co) | `g4f.Provider.ChatBase` | ✔️ | ❌ | ✔️ | ![Inactive](https://img.shields.io/badge/Inactive-red) | ❌ |
| [chatgptdemo.info](https://chatgptdemo.info/chat) | `g4f.Provider.ChatgptDemo` | ✔️ | ❌ | ✔️ | ![Inactive](https://img.shields.io/badge/Inactive-red) | ❌ |
| [chat.chatgptdemo.ai](https://chat.chatgptdemo.ai) | `g4f.Provider.ChatgptDemoAi` | ✔️ | ❌ | ✔️ | ![Inactive](https://img.shields.io/badge/Inactive-red) | ❌ |
| [chatgptfree.ai](https://chatgptfree.ai) | `g4f.Provider.ChatgptFree` | ✔️ | ❌ | ❌ | ![Inactive](https://img.shields.io/badge/Inactive-red) | ❌ |
| [chatgptlogin.ai](https://chatgptlogin.ai) | `g4f.Provider.ChatgptLogin` | ✔️ | ❌ | ✔️ | ![Inactive](https://img.shields.io/badge/Inactive-red) | ❌ |
| [chat.3211000.xyz](https://chat.3211000.xyz) | `g4f.Provider.Chatxyz` | ✔️ | ❌ | ✔️ | ![Inactive](https://img.shields.io/badge/Inactive-red) | ❌ |
| [gpt6.ai](https://gpt6.ai) | `g4f.Provider.Gpt6` | ✔️ | ❌ | ✔️ | ![Inactive](https://img.shields.io/badge/Inactive-red) | ❌ |
| [gptchatly.com](https://gptchatly.com) | `g4f.Provider.GptChatly` | ✔️ | ❌ | ❌ | ![Inactive](https://img.shields.io/badge/Inactive-red) | ❌ |
| [ai18.gptforlove.com](https://ai18.gptforlove.com) | `g4f.Provider.GptForLove` | ✔️ | ❌ | ✔️ | ![Inactive](https://img.shields.io/badge/Inactive-red) | ❌ |
| [gptgo.ai](https://gptgo.ai) | `g4f.Provider.GptGo` | ✔️ | ❌ | ✔️ | ![Inactive](https://img.shields.io/badge/Inactive-red) | ❌ |
| [gptgod.site](https://gptgod.site) | `g4f.Provider.GptGod` | ✔️ | ❌ | ✔️ | ![Inactive](https://img.shields.io/badge/Inactive-red) | ❌ |
| [onlinegpt.org](https://onlinegpt.org) | `g4f.Provider.OnlineGpt` | ✔️ | ❌ | ✔️ | ![Inactive](https://img.shields.io/badge/Inactive-red) | ❌ |

### Other

| Website | Provider | GPT-3.5 | GPT-4 | Stream | Status | Auth |
| ------  | -------  | ------- | ----- | ------ | ------ | ---- |
| [openchat.team](https://openchat.team) | `g4f.Provider.Aura` | ❌ | ❌ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [bard.google.com](https://bard.google.com) | `g4f.Provider.Bard` | ❌ | ❌ | ❌ | ![Unknown](https://img.shields.io/badge/Unknown-grey) | ✔️ |
| [deepinfra.com](https://deepinfra.com) | `g4f.Provider.DeepInfra` | ❌ | ❌ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [free.chatgpt.org.uk](https://free.chatgpt.org.uk) | `g4f.Provider.FreeChatgpt` | ❌ | ❌ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [gemini.google.com](https://gemini.google.com) | `g4f.Provider.Gemini` | ❌ | ❌ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ✔️ |
| [ai.google.dev](https://ai.google.dev) | `g4f.Provider.GeminiPro` | ❌ | ❌ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ✔️ |
| [gemini-chatbot-sigma.vercel.app](https://gemini-chatbot-sigma.vercel.app) | `g4f.Provider.GeminiProChat` | ❌ | ❌ | ✔️ | ![Unknown](https://img.shields.io/badge/Unknown-grey) | ❌ |
| [huggingface.co](https://huggingface.co/chat) | `g4f.Provider.HuggingChat` | ❌ | ❌ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [huggingface.co](https://huggingface.co/chat) | `g4f.Provider.HuggingFace` | ❌ | ❌ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [llama2.ai](https://www.llama2.ai) | `g4f.Provider.Llama2` | ❌ | ❌ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [labs.perplexity.ai](https://labs.perplexity.ai) | `g4f.Provider.PerplexityLabs` | ❌ | ❌ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [pi.ai](https://pi.ai/talk) | `g4f.Provider.Pi` | ❌ | ❌ | ✔️ | ![Active](https://img.shields.io/badge/Active-brightgreen) | ❌ |
| [theb.ai](https://theb.ai) | `g4f.Provider.ThebApi` | ❌ | ❌ | ❌ | ![Unknown](https://img.shields.io/badge/Unknown-grey) | ✔️ |
| [open-assistant.io](https://open-assistant.io/chat) | `g4f.Provider.OpenAssistant` | ❌ | ❌ | ✔️ | ![Inactive](https://img.shields.io/badge/Inactive-red) | ✔️ |

### Models

| Model | Base Provider | Provider | Website |
| ----- | ------------- | -------- | ------- |
| gpt-3.5-turbo | OpenAI | 5+ Providers | [openai.com](https://openai.com/) |
| gpt-4 | OpenAI | 2+ Providers | [openai.com](https://openai.com/) |
| gpt-4-turbo | OpenAI | g4f.Provider.Bing | [openai.com](https://openai.com/) |
| Llama-2-7b-chat-hf | Meta | 2+ Providers | [llama.meta.com](https://llama.meta.com/) |
| Llama-2-13b-chat-hf | Meta | 2+ Providers | [llama.meta.com](https://llama.meta.com/) |
| Llama-2-70b-chat-hf | Meta | 3+ Providers | [llama.meta.com](https://llama.meta.com/) |
| CodeLlama-34b-Instruct-hf | Meta | 2+ Providers | [llama.meta.com](https://llama.meta.com/) |
| CodeLlama-70b-Instruct-hf | Meta | 2+ Providers | [llama.meta.com](https://llama.meta.com/) |
| Mixtral-8x7B-Instruct-v0.1 | Huggingface | 4+ Providers | [huggingface.co](https://huggingface.co/) |
| Mistral-7B-Instruct-v0.1 | Huggingface | 4+ Providers | [huggingface.co](https://huggingface.co/) |
| dolphin-2.6-mixtral-8x7b | Huggingface | g4f.Provider.DeepInfra | [huggingface.co](https://huggingface.co/) |
| lzlv_70b_fp16_hf | Huggingface | g4f.Provider.DeepInfra | [huggingface.co](https://huggingface.co/) |
| airoboros-70b | Huggingface | g4f.Provider.DeepInfra | [huggingface.co](https://huggingface.co/) |
| airoboros-l2-70b-gpt4-1.4.1 | Huggingface | g4f.Provider.DeepInfra | [huggingface.co](https://huggingface.co/) |
| openchat_3.5 | Huggingface | 2+ Providers | [huggingface.co](https://huggingface.co/) |
| gemini | Google | g4f.Provider.Gemini | [gemini.google.com](https://gemini.google.com/) |
| gemini-pro | Google | 2+ Providers | [gemini.google.com](https://gemini.google.com/) |
| claude-v2 | Anthropic | 1+ Providers | [anthropic.com](https://www.anthropic.com/) |
| claude-3-opus | Anthropic | g4f.Provider.You | [anthropic.com](https://www.anthropic.com/) |
| claude-3-sonnet | Anthropic | g4f.Provider.You | [anthropic.com](https://www.anthropic.com/) |
| pi | Inflection | g4f.Provider.Pi | [inflection.ai](https://inflection.ai/) |

## 🔗 Related GPT4Free Projects

<table>
  <thead align="center">
    <tr border: none;>
      <td><b>🎁 Projects</b></td>
      <td><b>⭐ Stars</b></td>
      <td><b>📚 Forks</b></td>
      <td><b>🛎 Issues</b></td>
      <td><b>📬 Pull requests</b></td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="https://github.com/xtekky/gpt4free"><b>gpt4free</b></a></td>
      <td><a href="https://github.com/xtekky/gpt4free/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/xtekky/gpt4free?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/xtekky/gpt4free/network/members"><img alt="Forks" src="https://img.shields.io/github/forks/xtekky/gpt4free?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/xtekky/gpt4free/issues"><img alt="Issues" src="https://img.shields.io/github/issues/xtekky/gpt4free?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/xtekky/gpt4free/pulls"><img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/xtekky/gpt4free?style=flat-square&labelColor=343b41"/></a></td>
    </tr>
      <td><a href="https://github.com/xiangsx/gpt4free-ts"><b>gpt4free-ts</b></a></td>
      <td><a href="https://github.com/xiangsx/gpt4free-ts/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/xiangsx/gpt4free-ts?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/xiangsx/gpt4free-ts/network/members"><img alt="Forks" src="https://img.shields.io/github/forks/xiangsx/gpt4free-ts?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/xiangsx/gpt4free-ts/issues"><img alt="Issues" src="https://img.shields.io/github/issues/xiangsx/gpt4free-ts?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/xiangsx/gpt4free-ts/pulls"><img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/xiangsx/gpt4free-ts?style=flat-square&labelColor=343b41"/></a></td>
    </tr>
     <tr>
      <td><a href="https://github.com/zukixa/cool-ai-stuff/"><b>Free AI API's & Potential Providers List</b></a></td>
      <td><a href="https://github.com/zukixa/cool-ai-stuff/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/zukixa/cool-ai-stuff?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/zukixa/cool-ai-stuff/network/members"><img alt="Forks" src="https://img.shields.io/github/forks/zukixa/cool-ai-stuff?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/zukixa/cool-ai-stuff/issues"><img alt="Issues" src="https://img.shields.io/github/issues/zukixa/cool-ai-stuff?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/zukixa/cool-ai-stuff/pulls"><img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/zukixa/cool-ai-stuff?style=flat-square&labelColor=343b41"/></a></td>
    </tr>
    <tr>
    <tr>
      <td><a href="https://github.com/xtekky/chatgpt-clone"><b>ChatGPT-Clone</b></a></td>
      <td><a href="https://github.com/xtekky/chatgpt-clone/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/xtekky/chatgpt-clone?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/xtekky/chatgpt-clone/network/members"><img alt="Forks" src="https://img.shields.io/github/forks/xtekky/chatgpt-clone?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/xtekky/chatgpt-clone/issues"><img alt="Issues" src="https://img.shields.io/github/issues/xtekky/chatgpt-clone?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/xtekky/chatgpt-clone/pulls"><img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/xtekky/chatgpt-clone?style=flat-square&labelColor=343b41"/></a></td>
    </tr>
    <tr>
      <td><a href="https://github.com/mishalhossin/Discord-Chatbot-Gpt4Free"><b>ChatGpt Discord Bot</b></a></td>
      <td><a href="https://github.com/mishalhossin/Discord-Chatbot-Gpt4Free/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/mishalhossin/Discord-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/mishalhossin/Discord-Chatbot-Gpt4Free/network/members"><img alt="Forks" src="https://img.shields.io/github/forks/mishalhossin/Discord-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/mishalhossin/Discord-Chatbot-Gpt4Free/issues"><img alt="Issues" src="https://img.shields.io/github/issues/mishalhossin/Discord-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/mishalhossin/Coding-Chatbot-Gpt4Free/pulls"><img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/mishalhossin/Discord-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41"/></a></td>
<tr>
        <tr>
      <td><a href="https://github.com/Zero6992/chatGPT-discord-bot"><b>chatGPT-discord-bot</b></a></td>
      <td><a href="https://github.com/Zero6992/chatGPT-discord-bot/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/Zero6992/chatGPT-discord-bot?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/Zero6992/chatGPT-discord-bot/network/members"><img alt="Forks" src="https://img.shields.io/github/forks/Zero6992/chatGPT-discord-bot?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/Zero6992/chatGPT-discord-bot/issues"><img alt="Issues" src="https://img.shields.io/github/issues/Zero6992/chatGPT-discord-bot?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/Zero6992/chatGPT-discord-bot/pulls"><img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/Zero6992/chatGPT-discord-bot?style=flat-square&labelColor=343b41"/></a></td>
<tr>
  <td><a href="https://github.com/SamirXR/Nyx-Bot"><b>Nyx-Bot (Discord)</b></a></td>
  <td><a href="https://github.com/SamirXR/Nyx-Bot/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/SamirXR/Nyx-Bot?style=flat-square&labelColor=343b41"/></a></td>
  <td><a href="https://github.com/SamirXR/Nyx-Bot/network/members"><img alt="Forks" src="https://img.shields.io/github/forks/SamirXR/Nyx-Bot?style=flat-square&labelColor=343b41"/></a></td>
  <td><a href="https://github.com/SamirXR/Nyx-Bot/issues"><img alt="Issues" src="https://img.shields.io/github/issues/SamirXR/Nyx-Bot?style=flat-square&labelColor=343b41"/></a></td>
  <td><a href="https://github.com/SamirXR/Nyx-Bot/pulls"><img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/SamirXR/Nyx-Bot?style=flat-square&labelColor=343b41"/></a></td>
</tr>
    </tr>
    <tr>
      <td><a href="https://github.com/MIDORIBIN/langchain-gpt4free"><b>LangChain gpt4free</b></a></td>
      <td><a href="https://github.com/MIDORIBIN/langchain-gpt4free/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/MIDORIBIN/langchain-gpt4free?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/MIDORIBIN/langchain-gpt4free/network/members"><img alt="Forks" src="https://img.shields.io/github/forks/MIDORIBIN/langchain-gpt4free?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/MIDORIBIN/langchain-gpt4free/issues"><img alt="Issues" src="https://img.shields.io/github/issues/MIDORIBIN/langchain-gpt4free?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/MIDORIBIN/langchain-gpt4free/pulls"><img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/MIDORIBIN/langchain-gpt4free?style=flat-square&labelColor=343b41"/></a></td>
    </tr>
    <tr>
      <td><a href="https://github.com/HexyeDEV/Telegram-Chatbot-Gpt4Free"><b>ChatGpt Telegram Bot</b></a></td>
      <td><a href="https://github.com/HexyeDEV/Telegram-Chatbot-Gpt4Free/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/HexyeDEV/Telegram-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/HexyeDEV/Telegram-Chatbot-Gpt4Free/network/members"><img alt="Forks" src="https://img.shields.io/github/forks/HexyeDEV/Telegram-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/HexyeDEV/Telegram-Chatbot-Gpt4Free/issues"><img alt="Issues" src="https://img.shields.io/github/issues/HexyeDEV/Telegram-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/HexyeDEV/Telegram-Chatbot-Gpt4Free/pulls"><img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/HexyeDEV/Telegram-Chatbot-Gpt4Free?style=flat-square&labelColor=343b41"/></a></td>
    </tr>
        <tr>
      <td><a href="https://github.com/Lin-jun-xiang/chatgpt-line-bot"><b>ChatGpt Line Bot</b></a></td>
      <td><a href="https://github.com/Lin-jun-xiang/chatgpt-line-bot/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/Lin-jun-xiang/chatgpt-line-bot?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/Lin-jun-xiang/chatgpt-line-bot/network/members"><img alt="Forks" src="https://img.shields.io/github/forks/Lin-jun-xiang/chatgpt-line-bot?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/Lin-jun-xiang/chatgpt-line-bot/issues"><img alt="Issues" src="https://img.shields.io/github/issues/Lin-jun-xiang/chatgpt-line-bot?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/Lin-jun-xiang/chatgpt-line-bot/pulls"><img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/Lin-jun-xiang/chatgpt-line-bot?style=flat-square&labelColor=343b41"/></a></td>
    </tr>
    <tr>
      <td><a href="https://github.com/Lin-jun-xiang/action-translate-readme"><b>Action Translate Readme</b></a></td>
      <td><a href="https://github.com/Lin-jun-xiang/action-translate-readme/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/Lin-jun-xiang/action-translate-readme?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/Lin-jun-xiang/action-translate-readme/network/members"><img alt="Forks" src="https://img.shields.io/github/forks/Lin-jun-xiang/action-translate-readme?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/Lin-jun-xiang/action-translate-readme/issues"><img alt="Issues" src="https://img.shields.io/github/issues/Lin-jun-xiang/action-translate-readme?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/Lin-jun-xiang/action-translate-readme/pulls"><img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/Lin-jun-xiang/action-translate-readme?style=flat-square&labelColor=343b41"/></a></td>
    </tr>
    <tr>
      <td><a href="https://github.com/Lin-jun-xiang/docGPT-streamlit"><b>Langchain Document GPT</b></a></td>
      <td><a href="https://github.com/Lin-jun-xiang/docGPT-streamlit/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/Lin-jun-xiang/docGPT-streamlit?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/Lin-jun-xiang/docGPT-streamlit/network/members"><img alt="Forks" src="https://img.shields.io/github/forks/Lin-jun-xiang/docGPT-streamlit?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/Lin-jun-xiang/docGPT-streamlit/issues"><img alt="Issues" src="https://img.shields.io/github/issues/Lin-jun-xiang/docGPT-streamlit?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/Lin-jun-xiang/docGPT-streamlit/pulls"><img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/Lin-jun-xiang/docGPT-streamlit?style=flat-square&labelColor=343b41"/></a></td>
    </tr>
    <tr>
      <td><a href="https://github.com/Simatwa/python-tgpt"><b>python-tgpt</b></a></td>
      <td><a href="https://github.com/Simatwa/python-tgpt/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/Simatwa/python-tgpt?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/Simatwa/python-tgpt/network/members"><img alt="Forks" src="https://img.shields.io/github/forks/Simatwa/python-tgpt?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/Simatwa/python-tgpt/issues"><img alt="Issues" src="https://img.shields.io/github/issues/Simatwa/python-tgpt?style=flat-square&labelColor=343b41"/></a></td>
      <td><a href="https://github.com/Simatwa/python-tgpt/pulls"><img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/Simatwa/python-tgpt?style=flat-square&labelColor=343b41"/></a></td>
    </tr>
  </tbody>
</table>

## 🤝 Contribute

We welcome contributions from the community. Whether you're adding new providers or features, or simply fixing typos and making small improvements, your input is valued. Creating a pull request is all it takes – our co-pilot will handle the code review process. Once all changes have been addressed, we'll merge the pull request into the main branch and release the updates at a later time.

###### Guide: How do i create a new Provider?

 - Read: [/docs/guides/create_provider](/docs/guides/create_provider.md)

###### Guide: How can AI help me with writing code?

 - Read: [/docs/guides/help_me](/docs/guides/help_me.md)

## 🙌 Contributors

A list of all contributors is available [here](https://github.com/xtekky/gpt4free/graphs/contributors)   
The [`Vercel.py`](https://github.com/xtekky/gpt4free/blob/main/g4f/Provider/Vercel.py) file contains code from [vercel-llm-api](https://github.com/ading2210/vercel-llm-api) by [@ading2210](https://github.com/ading2210), which is licensed under the [GNU GPL v3](https://www.gnu.org/licenses/gpl-3.0.txt)   
Top 1 Contributor: [@hlohaus](https://github.com/hlohaus)

## ©️ Copyright

This program is licensed under the [GNU GPL v3](https://www.gnu.org/licenses/gpl-3.0.txt)

```
xtekky/gpt4free: Copyright (C) 2023 xtekky

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
```

## ⭐ Star History

<a href="https://github.com/xtekky/gpt4free/stargazers">
        <img width="500" alt="Star History Chart" src="https://api.star-history.com/svg?repos=xtekky/gpt4free&type=Date">
</a>

</details>

## 📄 License

<table>
  <tr>
     <td>
       <p align="center"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/GPLv3_Logo.svg/1200px-GPLv3_Logo.svg.png" width="80%"></img>
    </td>
    <td> 
      <img src="https://img.shields.io/badge/License-GNU_GPL_v3.0-red.svg"/> <br> 
This project is licensed under <a href="./LICENSE">GNU_GPL_v3.0</a>.
    </td>
  </tr>
</table>

<p align="right">(<a href="#top">🔼 Back to top</a>)</p>
