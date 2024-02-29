from concurrent import futures
import logging

import grpc

from models.parse_pb2 import Status, ParseReply, Names, Granularity, MetaData, File, ParseDataResponse, Format
from models.parse_pb2_grpc import ParserServicer, add_ParserServicer_to_server
from analysis.analysisClient import AnalysisClient
from dataHandler import DataHandler
from config import RESTRICT_APPS


ALLOWED_APPS = ["petclinic", "plants"]


SUPPORTED_LANGUAGES = ["java", "python"]
CHUNK_SIZE = 1024


class ParsingServer(ParserServicer):
    def parseAll(self, request, context):
        logging.info("received request for parsing application {} in language {} !".format(request.appName,
                                                                                           request.language))
        analysis_client = AnalysisClient(request.appName, request.appRepo, request.language)
        level = Granularity.Name(request.level).lower() if request.HasField("level") else "class"
        data_handler = DataHandler(analysis_client, format=request.format)
        result = data_handler.load_all(level)
        status = Status.SUCCESS if not result else Status.FAILED
        reply = ParseReply(status=status)
        return reply

    def getNames(self, request, context):
        analysis_client = AnalysisClient(request.appName, request.appRepo, request.language)
        data_handler = DataHandler(analysis_client)
        names = data_handler.get_names(Granularity.Name(request.level).lower())
        reply = Names(names=names)
        return reply

    def getInteractions(self, request, context):
        name = "interactions"
        level = Granularity.Name(request.level).lower() if request.HasField("level") else "class"
        column_name = f"{level}_names"
        row_name = f"{level}_names"
        return self.return_data(request, name, column_name, row_name)

    def getCalls(self, request, context):
        name = "calls"
        level = Granularity.Name(request.level).lower() if request.HasField("level") else "class"
        column_name = f"{level}_names"
        row_name = f"{level}_names"
        return self.return_data(request, name, column_name, row_name)

    def getTFIDF(self, request, context):
        name = "tfidf"
        level = Granularity.Name(request.level).lower() if request.HasField("level") else "class"
        column_name = "vocabulary"
        row_name = f"{level}_names"
        return self.return_data(request, name, column_name, row_name)

    def getWordCounts(self, request, context):
        name = "word_count"
        level = Granularity.Name(request.level).lower() if request.HasField("level") else "class"
        column_name = f"{level}_names"
        row_name = f"{level}_names"
        return self.return_data(request, name, column_name, row_name)

    def return_data(self, request, name, column_name=None, row_name=None):
        logging.debug("Retrieving {} data".format(name))
        if RESTRICT_APPS and request.appName not in ALLOWED_APPS:
            raise ValueError(f"Unauthorized application {request.appName}. Please choose from the following options: "
                             f"{ALLOWED_APPS}")
        level = Granularity.Name(request.level).lower() if request.HasField("level") else "class"
        analysis_client = AnalysisClient(request.appName, request.appRepo, request.language)
        data_handler = DataHandler(analysis_client)
        path, data = data_handler.get_data(name, level)
        format = request.format if request.format else data_handler.DATA_FORMAT
        metadata = MetaData(status=Status.PENDING, name=name, format=format, column_index=0,
                            row_index=0, column_name=column_name, row_name=row_name)
        response = ParseDataResponse(metadata=metadata)
        logging.debug("Generating response for {} data".format(name))
        yield response
        if request.format and request.format != data_handler.DATA_FORMAT:
            data_chunks = data_handler.convert(path, data, request.format)
            with data_chunks as f:
                while True:
                    chunk = f.read(CHUNK_SIZE)
                    if not chunk:
                        break
                    response = ParseDataResponse(file=File(content=chunk))
                    yield response
        else:
            with open(path, "rb") as f:
                while True:
                    chunk = f.read(CHUNK_SIZE)
                    if not chunk:
                        break
                    response = ParseDataResponse(file=File(content=chunk))
                    yield response


def serve():
    port = '50500'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_ParserServicer_to_server(ParsingServer(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    logging.info("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    serve()
