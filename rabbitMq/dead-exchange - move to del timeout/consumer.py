import pika
from pika.exchange_type import ExchangeType

def callbackalt(ch, method, properties, body):
    print(f" [x] Alt Received {body.decode()}")

def callbackmain(ch, method, properties, body):
    print(f" [x] Main Received {body.decode()}")

connection_params = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()
channel.exchange_declare(exchange='altexexchange', exchange_type=ExchangeType.fanout)
channel.exchange_declare(exchange='mainexchange', exchange_type=ExchangeType.direct, arguments={'alternate-exchange': 'altexexchange'})

channel.queue_declare(queue='altexexchangequeue')
channel.queue_bind(queue='altexexchangequeue', exchange='altexexchange')
channel.basic_consume(queue='altexexchangequeue', on_message_callback=callbackalt, auto_ack=True)

channel.queue_declare(queue='mainexchangequeue')
channel.queue_bind(queue='mainexchangequeue', exchange='mainexchange', routing_key='test')
channel.basic_consume(queue='mainexchangequeue', on_message_callback=callbackmain, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()