import pika
import time
import random
import uuid
from pika.exchange_type import ExchangeType

def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")
    ch.basic_publish(
        '', 
        routing_key=properties.reply_to, 
        body=f"Reply: {body.decode()}", 
        properties=pika.BasicProperties(correlation_id=properties.correlation_id))

connection_params = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()
channel.queue_declare(queue='rpc_queue')
channel.basic_consume(queue='rpc_queue', auto_ack=True, on_message_callback=callback)

print(f" [*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()