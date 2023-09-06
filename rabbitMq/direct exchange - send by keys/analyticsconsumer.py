import pika
from pika.exchange_type import ExchangeType

def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")

connection_params = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()
channel.exchange_declare(exchange='routing', exchange_type=ExchangeType.direct)
queue = channel.queue_declare(queue='', exclusive=True)
queue_name = queue.method.queue
channel.queue_bind(exchange='routing', queue=queue_name, routing_key='delivery')
channel.queue_bind(exchange='routing', queue=queue_name, routing_key='payments')
channel.basic_consume(queue=queue_name, auto_ack=True, on_message_callback=callback)

print(f" [*] Waiting for messages. To exit press CTRL+C")

channel.start_consuming()