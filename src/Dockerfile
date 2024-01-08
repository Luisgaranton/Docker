FROM python:3.10

RUN apt-get update && apt-get install -y python3-pip

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "app.py", "--port=5000"]