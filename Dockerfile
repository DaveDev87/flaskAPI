FROM python:3.8.2

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]