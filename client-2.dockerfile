FROM python:3.12.0b3-alpine3.18
WORKDIR /chat-client-2
COPY client-2.py .
RUN pip install pika
CMD ["python", "client-2.py"]