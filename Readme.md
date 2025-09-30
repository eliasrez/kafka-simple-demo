
# kafka-demo

#### Kafka docker doc: https://developer.confluent.io/confluent-tutorials/kafka-on-docker/

##### Useful commands : see doc https://docs.confluent.io/kafka/operations-tools/kafka-tools.html

## Install confluent-kafka dependency
```
> pip3 install confluent-kafka
```


## Validate that the topic was created in kafka container
```
> docker exec -it kafka kafka-topics --list --bootstrap-server localhost:9092
orders 
```


## Describe that topic and see its partitions
```
> docker exec -it kafka kafka-topics --bootstrap-server localhost:9092 --describe --topic orders

Topic: orders   TopicId: eDdSvdd9SIyBjRm2ZrPQTA PartitionCount: 1       ReplicationFactor: 1    Configs: 
        Topic: orders   Partition: 0    Leader: 1       Replicas: 1     Isr: 1  Elr:    LastKnownElr: 
```

## List consumed topic events
```
> docker exec -it kafka kafka-console-consumer --bootstrap-server localhost:9092 --topic orders --from-beginning

{"order_id": "eee92c7a-dd9d-4530-8647-8b344a1e2ef7", "product_id": "product_id", "item": "mushroom pizza", "quantity": 2}
{"order_id": "c9f72406-b363-4071-9a0c-0ec60809a121", "product_id": "product_id", "item": "mushroom pizza", "quantity": 2}
```
``` 
