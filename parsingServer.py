from concurrent import futures
import logging
import os

import grpc

from decparsing.models import parse_pb2 as ppb
from decparsing.models import parse_pb2_grpc as ppbg
from decparsing.analysis.analysisClient import AnalysisClient
from decparsing.dataHandler import DataHandler
from decparsing.config import RESTRICT_APPS


ALLOWED_APPS = ["petclinic", "plants"]


SUPPORTED_LANGUAGES = ["java", "python"]
CHUNK_SIZE = 1024
DEFAULT_PORT = 50500


class ParsingServer(ppbg.ParserServicer):
    def parseAll(self, request, context):
        logging.info("received request for parsing application {} in language {} !".format(request.appName,
                                                                                           request.language))
        is_distributed = request.isDistributed if request.HasField("isDistributed") else False
        analysis_client = AnalysisClient(request.appName, request.appRepo, request.language,
                                         is_distributed=is_distributed)
        level = ppb.Granularity.Name(request.level).lower() if request.HasField("level") else "class"
        data_handler = DataHandler(analysis_client, format=request.format)
        result = data_handler.load_all(level)
        status = ppb.Status.SUCCESS if not result else ppb.Status.FAILED
        reply = ppb.ParseReply(status=status)
        return reply

    def getNames(self, request, context):
        is_distributed = request.isDistributed if request.HasField("isDistributed") else False
        analysis_client = AnalysisClient(request.appName, request.appRepo, request.language,
                                         is_distributed=is_distributed)
        data_handler = DataHandler(analysis_client)
        names = data_handler.get_names(ppb.Granularity.Name(request.level).lower())
        reply = ppb.Names(names=names)
        return reply

    def getInteractions(self, request, context):
        name = "interactions"
        level = ppb.Granularity.Name(request.level).lower() if request.HasField("level") else "class"
        column_name = f"{level}_names"
        row_name = f"{level}_names"
        return self.return_data(request, name, column_name, row_name)

    def getCalls(self, request, context):
        name = "calls"
        level = ppb.Granularity.Name(request.level).lower() if request.HasField("level") else "class"
        column_name = f"{level}_names"
        row_name = f"{level}_names"
        return self.return_data(request, name, column_name, row_name)

    def getTFIDF(self, request, context):
        name = "tfidf"
        level = ppb.Granularity.Name(request.level).lower() if request.HasField("level") else "class"
        column_name = "vocabulary"
        row_name = f"{level}_names"
        return self.return_data(request, name, column_name, row_name)

    def getWordCounts(self, request, context):
        name = "word_count"
        level = ppb.Granularity.Name(request.level).lower() if request.HasField("level") else "class"
        column_name = f"{level}_names"
        row_name = f"{level}_names"
        return self.return_data(request, name, column_name, row_name)

    def return_data(self, request, name, column_name=None, row_name=None):
        logging.debug("Retrieving {} data".format(name))
        if RESTRICT_APPS and request.appName not in ALLOWED_APPS:
            raise ValueError(f"Unauthorized application {request.appName}. Please choose from the following options: "
                             f"{ALLOWED_APPS}")
        level = ppb.Granularity.Name(request.level).lower() if request.HasField("level") else "class"
        is_distributed = request.isDistributed if request.HasField("isDistributed") else False
        analysis_client = AnalysisClient(request.appName, request.appRepo, request.language,
                                         is_distributed=is_distributed)
        data_handler = DataHandler(analysis_client)
        path, data = data_handler.get_data(name, level)
        format = request.format if request.format else data_handler.DATA_FORMAT
        metadata = ppb.MetaData(status=ppb.Status.PENDING, name=name, format=format, column_index=0,
                            row_index=0, column_name=column_name, row_name=row_name)
        response = ppb.ParseDataResponse(metadata=metadata)
        logging.debug("Generating response for {} data".format(name))
        yield response
        if request.format and request.format != data_handler.DATA_FORMAT:
            data_chunks = data_handler.convert(path, data, request.format)
            with data_chunks as f:
                while True:
                    chunk = f.read(CHUNK_SIZE)
                    if not chunk:
                        break
                    response = ppb.ParseDataResponse(file=ppb.File(content=chunk))
                    yield response
        else:
            with open(path, "rb") as f:
                while True:
                    chunk = f.read(CHUNK_SIZE)
                    if not chunk:
                        break
                    response = ppb.ParseDataResponse(file=ppb.File(content=chunk))
                    yield response


def serve():
    port = str(os.getenv('SERVICE_PARSING_PORT', DEFAULT_PORT))
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ppbg.add_ParserServicer_to_server(ParsingServer(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    logging.info("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    serve()
