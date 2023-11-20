FROM python:3.9-slim

RUN mkdir /service
COPY protos/ /protos/
COPY parsers/ /service/parsers/
COPY models/ /service/models/
COPY analysis /service/analysis/
COPY dataHandler.py /service/dataHandler.py
COPY parsingServer.py /service/parsingServer.py
COPY main.py /service/main.py
COPY cli.py /service/cli.py
COPY requirements.txt /service/requirements.txt
COPY data_prod/ /service/data/
WORKDIR /service
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m nltk.downloader stopwords

EXPOSE 50500
ENTRYPOINT [ "python", "main.py" ]