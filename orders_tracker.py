from confluent_kafka import Consumer
import json

consumer_config = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "orders-tracker",
    "auto.offset.reset": "earliest",
}

consumer = Consumer(consumer_config)

# Subscribe to the topics. Note this could be a list of topis
consumer.subscribe(["orders"])
print(f"🟢 Consumer is running and subscribed for orders topic")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print(f'Consumer error: {msg.error()}')
            continue
        value = msg.value().decode('utf-8')
        order = json.loads(value)
        print(f"📦Order received:{order['quantity']} x {order['item']} from user {order['user']}")

except KeyboardInterrupt:
    print(f"💔 Stopping Orders Tracker/Consumer")
finally:
    consumer.close()