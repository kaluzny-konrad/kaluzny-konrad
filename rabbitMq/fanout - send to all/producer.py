import pika
import time
import random
from pika.exchange_type import ExchangeType

connection_parameters = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
channel.exchange_declare(exchange='helloFan', exchange_type=ExchangeType.fanout)

messageId = 1

while True:
    message = 'Hello World: ' + str(messageId)
    channel.basic_publish(exchange='helloFan',
                        routing_key='',
                        body=message)
    print(" [x] Sent: " + message)
    time.sleep(random.randint(1, 4))
    messageId += 1