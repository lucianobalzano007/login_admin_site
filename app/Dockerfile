FROM python:3.13-alpine

WORKDIR /app

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY application.py /app
COPY templates /app/templates
COPY static /app/static
COPY crypto.py /app
COPY user.py /app
COPY mongo_connection.py /app

EXPOSE 5000

CMD ["python3", "application.py"]
