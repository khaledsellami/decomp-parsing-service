FROM python:3.9-slim

RUN mkdir /service
COPY protos/ /protos/
#COPY data_prod/ /service/data/
WORKDIR /service
COPY . .
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m nltk.downloader stopwords

EXPOSE 50500
ENTRYPOINT [ "python", "main.py" ]