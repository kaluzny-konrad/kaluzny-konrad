import pika
import time
import random
from pika.exchange_type import ExchangeType

def callback(ch, method, properties, body):
    processing_time = random.randint(1, 5)
    print(f"1 received: {body}, processing time: {processing_time}")
    time.sleep(processing_time)
    print("done")

connection_parameters = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
channel.exchange_declare(exchange='helloFan', exchange_type=ExchangeType.fanout)
queue = channel.queue_declare(queue='', exclusive=True)

channel.queue_bind(exchange='helloFan', queue=queue.method.queue)

channel.basic_consume(on_message_callback=callback,
                        queue=queue.method.queue, auto_ack=True)

print("Starting Consuming")

channel.start_consuming()