import pika
from pika.exchange_type import ExchangeType

connection_params = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# exchange to exchange pattern: direct -> fanout
channel.exchange_declare(exchange='source', exchange_type=ExchangeType.direct)
channel.exchange_declare(exchange='destination', exchange_type=ExchangeType.fanout)
channel.exchange_bind(destination='destination', source='source')
channel.basic_publish(exchange='source', routing_key='', body='Hello World!')

print(f" [x] Sent 'Hello World!'")
connection.close()