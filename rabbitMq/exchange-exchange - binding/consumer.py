import pika
from pika.exchange_type import ExchangeType

def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")

connection_params = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()
channel.exchange_declare(exchange='destination', exchange_type=ExchangeType.fanout)
channel.queue_declare(queue='analytics')
channel.queue_bind(exchange='destination', queue='analytics')
channel.basic_consume(queue='analytics', auto_ack=True, on_message_callback=callback)

print(f" [*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()