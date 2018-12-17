import json
from datetime import datetime

import pika as pika

from helpers.date_transform import datetimeSerializer


class QueueService:

    def __init__(self, config):
        self.config = config

    def get_connection(self):
        rmq_url = 'amqp://{username}:{password}@{host}:{port}/%2F'.format(**self.config)
        return pika.BlockingConnection(pika.URLParameters(rmq_url))

    def push_to_exchange(self, exchange, exchange_type, message, message_properties=None):
        connection = self.get_connection()
        channel = connection.channel()
        channel.exchange_declare(exchange=exchange, exchange_type=exchange_type)
        pika_properties = pika.BasicProperties(**message_properties) if message_properties else None
        return channel.basic_publish(exchange=exchange, routing_key='', body=message, properties=pika_properties)

    async def enqueue(self, account):
        event = json.dumps(
            dict(**account, when=datetime.now()),
            default=datetimeSerializer
        )
        return self.push_to_exchange(self.config['exchange']['name'],
                                     self.config['exchange']['type'],
                                     event)
