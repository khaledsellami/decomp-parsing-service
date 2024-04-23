import argparse
import logging

from decparsing.dataHandler import DataHandler
from decparsing.models import parse_pb2 as ppb
from decparsing.config import RESTRICT_APPS, DEFAULT_JAR_PATH
from decparsing import select_client


ALLOWED_APPS = ["petclinic", "plants"]


def cli(args):
    app_name = args.APP
    if RESTRICT_APPS and app_name not in ALLOWED_APPS:
        raise ValueError(f"Unauthorized application {app_name}. Please choose from the following options: "
                         f"{ALLOWED_APPS}")
    data_path = args.data
    output_path = args.output
    jar_path = args.jar
    use_jar = args.use_jar
    level = args.level
    is_distributed = args.is_distributed
    parsing_path = args.parsing_data
    format = ppb.Format.Value(args.format)
    client = select_client(app_name, data_path, use_jar, jar_path, is_distributed, parsing_path)
    data_handler = DataHandler(client, format=format, output_path=output_path)
    data_handler.load_all(level)


if __name__ == "__main__":
    # Parsing input
    parser = argparse.ArgumentParser(
        prog='parse',
        description='Parse the static analysis results of an application and save the output')
    parser.add_argument('APP', type=str, help='application to decompose')
    parser.add_argument("-d", "--data", type=str,
                        help='path for source code or github link to the source code')
    parser.add_argument("-o", "--output", help='path for the output', type=str, default="./output")
    parser.add_argument("-f", "--format", help='format of the data to save or load', type=str,
                        choices=ppb.Format.keys(), default="PARQUET")
    parser.add_argument("-j", "--jar", help='path for the analysis jar file', type=str,
                        default=DEFAULT_JAR_PATH)
    parser.add_argument("-u", "--use_jar", help='use the jar client', action="store_true")
    parser.add_argument("-l", "--level", help='granularity level of the analysis', type=str,
                        default="class", choices=["class", "method"])
    parser.add_argument("-D", "--is_distributed", action="store_true",
                        help='True is the application has a distributed architecture')
    parser.add_argument("-p", "--parsing-data", type=str,
                        help='path to existing parsing data', default=None)
    args = parser.parse_args()
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    cli(args)