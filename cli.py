import argparse
import logging

from analysis.analysisClient import AnalysisClient
from analysis.analysisLocalClient import AnalysisLocalClient
from analysis.analysisJarClient import AnalysisJarClient
from dataHandler import DataHandler

from models import parse_pb2 as ppb
from config import RESTRICT_APPS, DEFAULT_JAR_PATH


ALLOWED_APPS = ["petclinic", "plants"]


def cli(args):
    app_name = args.APP
    if RESTRICT_APPS and app_name not in ALLOWED_APPS:
        raise ValueError(f"Unauthorized application {app_name}. Please choose from the following options: "
                         f"{ALLOWED_APPS}")
    data_path = args.data
    from_source = args.source
    output_path = args.output
    jar_path = args.jar
    use_jar = args.use_jar
    level = args.level
    format = ppb.Format.Value(args.format)
    if from_source:
        if use_jar:
            client = AnalysisJarClient(app_name, data_path, jar_path)
        else:
            client = AnalysisClient(app_name, data_path)
    else:
        if data_path is None:
            client = AnalysisClient(app_name, "")
        else:
            client = AnalysisLocalClient(app_name, data_path)
    data_handler = DataHandler(client, format=format, output_path=output_path)
    data_handler.load_all(level)


if __name__ == "__main__":
    # Parsing input
    parser = argparse.ArgumentParser(
        prog='parse',
        description='Parse the static analysis results of an application and save the output')
    parser.add_argument('APP', type=str, help='application to decompose')
    parser.add_argument("-d", "--data", type=str,
                        help='path for the static analysis data or source code or link to the source code')
    parser.add_argument("-o", "--output", help='path for the output', type=str, default="./output")
    parser.add_argument("-f", "--format", help='format of the data to save or load', type=str,
                        choices=ppb.Format.keys(), default="PARQUET")
    parser.add_argument("-j", "--jar", help='path for the analysis jar file', type=str,
                        default=DEFAULT_JAR_PATH)
    parser.add_argument("-s", "--source", help='use the data input as source code', action="store_true")
    parser.add_argument("-u", "--use_jar", help='use the jar client', action="store_true")
    parser.add_argument("-l", "--level", help='granularity level of the analysis', type=str,
                        default="class", choices=["class", "method"])
    args = parser.parse_args()
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    cli(args)