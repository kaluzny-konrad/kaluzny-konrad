import pika
from pika.exchange_type import ExchangeType

def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")

connection_params = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()
channel.exchange_declare(exchange='mainexchange-dead', exchange_type=ExchangeType.direct)
message = 'Hello World!'
channel.basic_publish(exchange='mainexchange-dead', routing_key='test', body=message)
print(f" [x] Sent '{message}'")
connection.close()