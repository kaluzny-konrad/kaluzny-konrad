import pika
import time
import random

connection_parameters = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()
channel.queue_declare(queue='hello')

messageId = 1

while True:
    message = 'Hello World: ' + str(messageId)
    channel.basic_publish(exchange='',
                        routing_key='hello',
                        body=message)
    print(" [x] Sent: " + message)
    time.sleep(random.randint(1, 4))
    messageId += 1