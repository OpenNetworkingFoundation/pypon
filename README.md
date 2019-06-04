# openoltd

openoltd - A simple controller for  PON Optical Line Terminals (OLTs) that support the VOLTHA project's Openolt api.

## Install
### Install and start Confluent Kafka
### Install openoltd
```
pip install openoltd
```
## Develop
```
git clone git@github.com:shadansari/openolt.git
cd openolt
pipenv shell
pipenv install
make protos
```

## Test
### Start openoltd
```
openoltd <olt ip address>
```

### Read openolt indications from kafka
```
confluent-kafka/consumer.py localhost:9092 foo openolt.ind-<olt ip address>
```
