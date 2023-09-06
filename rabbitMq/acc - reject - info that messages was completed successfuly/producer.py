import pika
from pika.exchange_type import ExchangeType

def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")

connection_params = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()
channel.exchange_declare(exchange='accexchange', exchange_type=ExchangeType.fanout)
message = 'Hello World!'
while True:
    channel.basic_publish(exchange='accexchange', routing_key='test', body=message)
    print(f" [x] Sent '{message}'")
    message = input('Enter message: ')