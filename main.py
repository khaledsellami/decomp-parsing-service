import argparse
import logging

from cli import cli
from parsingServer import serve
from models import parse_pb2 as ppb
from config import DEFAULT_JAR_PATH


def main():
    # Parsing input
    parser = argparse.ArgumentParser(
        prog='parser',
        description='Parse the static analysis results of an application')
    subparsers = parser.add_subparsers(dest="subtask", required=False)
    cli_parser = subparsers.add_parser("parse", description="parse and save an application")
    cli_parser.add_argument('APP', type=str, help='application to decompose')
    cli_parser.add_argument("-d", "--data", help='path for the static analysis data', type=str)
    cli_parser.add_argument("-o", "--output", help='path for the output', type=str, default="./output")
    cli_parser.add_argument("-f", "--format", help='format of the data to save or load', type=str,
                        choices=ppb.Format.keys(), default="PARQUET")
    cli_parser.add_argument("-j", "--jar", help='path for the analysis jar file', type=str,
                        default=DEFAULT_JAR_PATH)
    cli_parser.add_argument("-s", "--source", help='use the data input as source code', action="store_true")
    cli_parser.add_argument("-u", "--use_jar", help='use the jar client', action="store_true")
    cli_parser.add_argument("-l", "--level", help='granularity level of the analysis', type=str,
                        default="class", choices=["class", "method"])
    subparsers.add_parser("start", description="start the parsing server")
    args = parser.parse_args()
    # route the task
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    if args.subtask is None or args.subtask == "start":
        serve()
    elif args.subtask == "parse":
        cli(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()