FROM python:3.10.6

WORKDIR /app
COPY requerimentes.txt /app/requerimentes.txt

RUN pip install --no-cache-dir --upgrade -r /app/requerimentes.txt

COPY . /app

CMD bash -c "while true; do sleep 1; done"