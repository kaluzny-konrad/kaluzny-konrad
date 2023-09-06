import pika
import time
import random
import uuid
from pika.exchange_type import ExchangeType

def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")
    channel.stop_consuming()

connection_params = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()
reply_queue = channel.queue_declare(queue='', exclusive=True)
reply_queue_name = reply_queue.method.queue


while True:
    channel.basic_consume(queue=reply_queue_name, auto_ack=True, on_message_callback=callback)
    channel.queue_declare(queue='rpc_queue')
    message = f"Hello World: {random.randint(1, 100)}"
    correlation_id = str(uuid.uuid4())
    channel.basic_publish(
        exchange='', 
        routing_key='rpc_queue', 
        body=message, 
        properties=pika.BasicProperties(
            reply_to=reply_queue_name,
            correlation_id=correlation_id))

    print(f" [x] Sent {message}")
    print(f" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()
    rand_wait = random.randint(1, 4)
    print(f" __________ Cooling Down for: {rand_wait}")
    time.sleep(rand_wait)
