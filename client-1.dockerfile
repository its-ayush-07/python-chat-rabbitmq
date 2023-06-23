FROM python:3.12.0b3-alpine3.18
WORKDIR /chat-client-1
COPY client-1.py .
RUN pip install pika
CMD ["python", "client-1.py"]