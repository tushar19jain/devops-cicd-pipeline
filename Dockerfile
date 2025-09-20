FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install flask

EXPOSE 5000

CMD [ "python","server.py" ]