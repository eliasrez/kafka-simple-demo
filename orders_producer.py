import json
import uuid
from confluent_kafka import Producer

producer_config = {
    'bootstrap.servers': 'localhost:9092'
}

producer = Producer(producer_config)


def delivery_report(err, msg):
    if err is not None:
        print(f'❌ Message delivery failed: {err}')
    else:
        print(f'✅ Message delivery succeeded: {msg.value().decode('utf-8')}')
        # print(dir(msg))
        print(f'📨 Delivered to {msg.topic()} partition: {msg.partition()} at offset: {msg.offset()} ')


order = {
    "order_id": str(uuid.uuid4()),
    "product_id": "product_id",
    "user": "Elias R",
    "item": "Hotdoc",
    "quantity": 2,
}

value = json.dumps(order).encode('utf-8')
producer.produce(topic='orders',
                 value=value,
                 callback=delivery_report)

producer.flush()
