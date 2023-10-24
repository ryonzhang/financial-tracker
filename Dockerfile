FROM python:3.8-alpine

WORKDIR /python-docker

RUN apk add postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8080
CMD [ "waitress-serve", "--port=8080", "--call", "app:create_app"]
