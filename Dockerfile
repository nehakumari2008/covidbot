FROM python:3
COPY . /pybot
WORKDIR /pybot
RUN pip install -r requirements.txt
ENTRYPOINT ["errbot"]

