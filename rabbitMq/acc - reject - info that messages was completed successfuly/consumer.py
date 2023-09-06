import pika
from pika.exchange_type import ExchangeType

def callback(ch, method, properties, body):
    ch.basic_ack(delivery_tag=method.delivery_tag, multiple=False)
    print(f" [x] Received {body.decode()}")


connection_params = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()
channel.exchange_declare(exchange='accexchange', exchange_type=ExchangeType.fanout)

channel.queue_declare(queue='accexchangequeue')
channel.queue_bind(queue='accexchangequeue', exchange='accexchange', routing_key='test')
channel.basic_consume(queue='accexchangequeue', on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()