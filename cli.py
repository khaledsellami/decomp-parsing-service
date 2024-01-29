import argparse
import logging

from analysis.analysisClient import AnalysisClient
from analysis.analysisLocalClient import AnalysisLocalClient
from dataHandler import DataHandler

from models.parse_pb2 import Format
from config import RESTRICT_APPS


ALLOWED_APPS = ["petclinic", "plants"]


def cli(args):
    app_name = args.APP
    if RESTRICT_APPS and app_name not in ALLOWED_APPS:
        raise ValueError(f"Unauthorized application {app_name}. Please choose from the following options: "
                         f"{ALLOWED_APPS}")
    data_path = args.data
    output_path = args.output
    format = Format.Value(args.format)
    if data_path is None:
        client = AnalysisClient(app_name, "")
    else:
        client = AnalysisLocalClient(app_name, data_path)
    data_handler = DataHandler(client, format=format, output_path=output_path)
    data_handler.load_all()


if __name__ == "__main__":
    # Parsing input
    parser = argparse.ArgumentParser(
        prog='parse',
        description='Parse the static analysis results of an application and save the output')
    parser.add_argument('APP', type=str, help='application to decompose')
    parser.add_argument("-d", "--data", help='path for the static analysis data', type=str)
    parser.add_argument("-o", "--output", help='path for the output', type=str, default="./output")
    parser.add_argument("-f", "--format", help='format of the data to save or load', type=str,
                        choices=Format.keys(), default="PARQUET")
    args = parser.parse_args()
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    cli(args)