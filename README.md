# openolt quickstart 
openolt is a collection of programs for managing Optical Line Terminals (OLTs) that support the VOLTHA project's Openolt api.

## Install and start Confluent Kafka
TODO - Add help and links to Confluent docs

## Install openolt
### Get the code
```
git clone git@github.com:shadansari/openolt.git
```

### Create the virtual env

All commands needs to run in a virtual env with PYTHONPATH set.

```
cd openolt
pipenv shell
export PYTHONPATH=$PYTHONPATH:$PWD:$PWD/protos/third_party
```

## Connect to OLT and publish events to Kafka
### Fetch openolt indications from the device and publish to Kafka
```
python openolt/sb_grpc.py localhost:9092 10.90.0.114:9191
```

### Read openolt indications from kafka
```
confluent-kafka/consumer.py localhost:9092 foo openolt.ind-10.90.0.114
```
