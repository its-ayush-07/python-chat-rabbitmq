import pika
import threading

# Connection parameters
connection_params = pika.ConnectionParameters('rabbitmq')

def consume_messages():
    """Callback function to handle consuming messages from RabbitMQ"""
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()
    channel.queue_declare(queue='queueA')

    def callback(ch, method, properties, body):
        print("Received:", body.decode())

    channel.basic_consume(queue='queueA', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

def publish_messages():
    """Function to publish messages to RabbitMQ"""
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()

    while True:
        message = input("Enter message: ")
        channel.basic_publish(exchange='', routing_key='queueB', body=message.encode())

# Start consuming messages in a separate thread
consume_thread = threading.Thread(target=consume_messages)
consume_thread.start()

# Start publishing messages in the main thread
publish_messages()
