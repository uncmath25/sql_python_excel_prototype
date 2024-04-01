FROM python:3.12.2-slim

USER root

COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

ARG SRC_DIR="src"
COPY ./$SRC_DIR /$SRC_DIR
ENV PYTHONPATH "$PYTHONPATH:/$SRC_DIR"
WORKDIR /$SRC_DIR

CMD python3 main.py
