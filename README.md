# ponster

ponster - A simple controller for  PON Optical Line Terminals (OLTs) that support the VOLTHA project's Openolt api.

## Install
### Install and start Confluent Kafka
### Install ponster
```
pip install ponster
```
## Develop
```
git clone git@github.com:shadansari/openolt.git
cd ponster 
pipenv shell
pipenv install
make protos
```

## Test
### Start ponster
```
ponster <olt ip address>
```

### Read openolt indications from kafka
```
confluent-kafka/consumer.py localhost:9092 foo openolt.ind-<olt ip address>
```
