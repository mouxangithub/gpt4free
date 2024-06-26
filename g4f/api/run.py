import g4f.api
from argparse import ArgumentParser
from g4f import Provider
from enum import Enum


def api_parser():
    IgnoredProviders = Enum("ignore_providers", {
        key: key for key in Provider.__all__})
    parser = ArgumentParser(description="Run the GUI")
    parser.add_argument("-host", type=str, default="0.0.0.0", help="hostname")
    parser.add_argument("-port", type=int, default=1337, help="port")
    parser.add_argument("-debug", action="store_true", help="debug mode")
    parser.add_argument("-ignored-providers", nargs="+", choices=[
        provider.name for provider in IgnoredProviders],
        default=[], help="List of providers to ignore when processing request.")
    return parser


def run_api_args(args):
    host = args.host
    port = args.port
    debug = args.debug
    ignored_providers = args.ignored_providers
    g4f.api.Api(
        engine=g4f,
        debug=debug,
        list_ignored_providers=ignored_providers
    ).run(host, port)


if __name__ == "__main__":
    parser = api_parser()
    args = parser.parse_args()
    run_api_args(args)
