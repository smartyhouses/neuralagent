FROM python:3.12
WORKDIR /app

COPY . /app

COPY requirements.txt /app/requirements.txt

RUN apt-get update -y

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--workers", "4"]