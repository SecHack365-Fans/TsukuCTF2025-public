FROM python:3.11-slim

RUN apt-get update && apt-get install -yqq socat

WORKDIR /app

COPY server.py .

EXPOSE 30057

CMD ["socat", "TCP-L:30057,fork,reuseaddr", "EXEC:'python server.py'"]
