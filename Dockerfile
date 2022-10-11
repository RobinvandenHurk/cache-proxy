FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

ENV PORT 5000
ENV CACHE_FILE /cache.session

CMD ["sh", "-c", "python3 proxy.py -p $PORT -s $CACHE_FILE"]

