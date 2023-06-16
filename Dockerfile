FROM python:3.9-slim

RUN mkdir /service
COPY protos/ /protos/
COPY parsers/ /service/parsers/
COPY models/ /service/models/
COPY dataHandler.py /service/dataHandler.py
COPY parsingServer.py /service/parsingServer.py
COPY analysisClient.py /service/analysisClient.py
COPY requirements.txt /service/requirements.txt
WORKDIR /service
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m nltk.downloader stopwords

EXPOSE 50500
ENTRYPOINT [ "python", "parsingServer.py" ]