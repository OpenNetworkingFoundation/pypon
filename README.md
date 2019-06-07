# ponstar

ponstar - A simple controller for  PON Optical Line Terminals (OLTs) that support the VOLTHA project's Openolt api.

## Install
### Install and start Confluent Kafka
### Install ponstar
```
pip install ponstar
```
## Develop
```
git clone git@github.com:shadansari/openolt.git
cd ponstar 
pipenv shell
pipenv install
make protos
```

## Test
### Start ponstar
```
ponstar <olt ip address>
```

### Read openolt indications from kafka
```
confluent-kafka/consumer.py localhost:9092 foo openolt.ind-<olt ip address>
```
