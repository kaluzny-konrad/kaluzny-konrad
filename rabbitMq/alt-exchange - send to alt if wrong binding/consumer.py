import pika
from pika.exchange_type import ExchangeType

def callbackdead(ch, method, properties, body):
    print(f" [x] Dead Received {body.decode()}")

connection_params = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()
channel.exchange_declare(exchange='maindlx', exchange_type=ExchangeType.direct)
channel.exchange_declare(exchange='dlx', exchange_type=ExchangeType.fanout)

channel.queue_declare(queue='maindlxqueue',
                      arguments={'x-letter-exchange': 'dlx', 'x-message-ttl': 1000})
channel.queue_bind(queue='maindlxqueue', exchange='maindlx', routing_key='test')

channel.queue_declare(queue='dlxqueue')
channel.queue_bind(queue='dlxqueue', exchange='dlx')

channel.basic_consume(queue='dlxqueue', on_message_callback=callbackdead, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()