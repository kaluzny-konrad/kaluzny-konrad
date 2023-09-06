import pika
from pika.exchange_type import ExchangeType

def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")

connection_params = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()
channel.exchange_declare(exchange='altexexchange', exchange_type=ExchangeType.fanout)
channel.exchange_declare(exchange='mainexchange', exchange_type=ExchangeType.direct, arguments={'alternate-exchange': 'altexexchange'})
message = 'Hello World!'
channel.basic_publish(exchange='mainexchange', routing_key='test', body=message)
print(f" [x] Sent '{message}'")
connection.close()