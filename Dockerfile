FROM python:3.9.16-slim-buster

LABEL authors="eriknathan"

RUN pip install python-dotenv

COPY ./lib /lib

COPY database.py .

COPY main.py .

ENTRYPOINT ["python3", "main.py"]