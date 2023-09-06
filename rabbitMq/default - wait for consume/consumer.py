import pika
import time
import random

connection_parameters = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    processing_time = random.randint(1, 5)
    print(f"received: {body}, processing time: {processing_time}")
    time.sleep(processing_time)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("done")

# channel.basic_qos(prefetch_count=1)

channel.basic_consume(on_message_callback=callback,
                        queue='hello')

print("Starting Consuming")

channel.start_consuming()