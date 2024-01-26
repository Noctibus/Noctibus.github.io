FROM python:3.11-slim-buster

WORKDIR /docker/PatentKeeper

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8082

CMD [ "python3", "main.py" ]