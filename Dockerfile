FROM python:3.8-alpine
COPY . /src
WORKDIR /src
RUN pip install -r requirements.txt
CMD flask --app src/web/run run
