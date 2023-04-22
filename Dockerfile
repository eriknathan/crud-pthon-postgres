FROM python:3.9.16-slim-buster
LABEL authors="eriknathan"

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

RUN pip install python-dotenv

COPY . .

CMD ["python3", "main.py"]