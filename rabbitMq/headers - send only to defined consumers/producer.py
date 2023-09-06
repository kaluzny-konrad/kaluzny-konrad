import pika
from pika.exchange_type import ExchangeType

connection_params = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# exchange to exchange pattern: direct -> fanout
channel.exchange_declare(exchange='headers', exchange_type=ExchangeType.headers)
channel.basic_publish(
    exchange='headers', 
    routing_key='', 
    body='Hello World!',
    properties=pika.BasicProperties(headers={'name': 'brian'}))

print(f" [x] Sent 'Hello World!'")
connection.close()