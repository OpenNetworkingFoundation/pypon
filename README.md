# olt-ctl quickstart 
olt-ctl is a collection of programs for managing Optical Line Terminals (OLTs) that support the VOLTHA project's Openolt api.

## Install and start Confluent Kafka
TODO - Add help and links to Confluent docs

## Install olt-ctl
### Get the code
```shell
git clone git@github.com:shadansari/olt-ctl.git
```

### Create the virtual env

All commands needs to run in a virtual env.

```shell
cd olt-ctl
source env.sh
```

## Connect to OLT and publish events to Kafka
### Fetch openolt indications from the device and publish to Kafka
```shell
python openolt/sb_grpc.py localhost:9092 10.90.0.114:9191
```


### Read openolt indications from kafka
```shell

confluent-kafka/consumer.py localhost:9092 foo openolt.ind-10.90.0.114
```
