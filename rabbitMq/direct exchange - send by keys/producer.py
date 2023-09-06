import pika
from pika.exchange_type import ExchangeType
import time
import random

connection_params = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()
channel.exchange_declare(exchange='routing', exchange_type=ExchangeType.direct)

n = 0
while True:
    message = f"Hello World: {n}"
    if(n % 2 == 0):
        message += " - delivery"
        channel.basic_publish(exchange='routing', routing_key='delivery', body=message)
    else:
        message += " - payments"
        channel.basic_publish(exchange='routing', routing_key='payments', body=message)
    print(f" [x] Sent {message}")
    n += 1
    time.sleep(random.randint(1, 4))