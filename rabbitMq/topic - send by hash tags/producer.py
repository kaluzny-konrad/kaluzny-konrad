import pika
from pika.exchange_type import ExchangeType
import time
import random

connection_params = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()
channel.exchange_declare(exchange='topicexchange', exchange_type=ExchangeType.topic)

n = 0
while True:
    message = f"Hello World: {n}"
    if(n % 4 == 0):
        message += " - business.africa.delivery"
        channel.basic_publish(exchange='topicexchange', routing_key='business.africa.delivery', body=message)
    if(n % 4 == 1):
        message += " - user.europe.delivery"
        channel.basic_publish(exchange='topicexchange', routing_key='user.europe.delivery', body=message)
    if(n % 4  == 2):
        message += " - business.europe.payments"
        channel.basic_publish(exchange='topicexchange', routing_key='business.europe.payments', body=message)
    if(n % 4  == 3):
        message += " - user.africa.payments"
        channel.basic_publish(exchange='topicexchange', routing_key='user.africa.payments', body=message)
    print(f" [x] Sent {message}")
    n += 1
    time.sleep(random.randint(1, 4))