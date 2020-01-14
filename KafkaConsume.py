import time

from kafka import KafkaConsumer
# from json import loads
import json


class KafkaToNSQ():
    def __init__(self, *args, **kwargs):
        pass

    def consume(self):
        consumer = KafkaConsumer(
            'testing',
            bootstrap_servers=['192.168.71.214:9092'],
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='testing-dummy'
            # value_deserializer=lambda x: loads(x.decode('utf-8'))
        )
        counter = 1
        for message in consumer:
            result = {}
            data = message.value
            print(data)
            # data = json.loads(data)
            # print(json.dumps(data))

if __name__ == '__main__':
    kafka = KafkaToNSQ()
    kafka.consume()
