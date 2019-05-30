#
# Copyright 2019 the original author or authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# import pdb
import sys
import grpc
import threading
from multiprocessing import Process
import structlog
from simplejson import dumps
from google.protobuf.json_format import MessageToJson

from protos.openolt import openolt_pb2_grpc, openolt_pb2
from confluent_kafka import Producer


log = structlog.get_logger()


class OpenoltGrpc(object):
    def __init__(self, host_and_port, device):
        super(OpenoltGrpc, self).__init__()
        log.debug('openolt grpc init')
        self.device = device
        self.host_and_port = host_and_port
        self.channel = grpc.insecure_channel(self.host_and_port)
        self.stub = openolt_pb2_grpc.OpenoltStub(self.channel)

    def start(self):
        try:
            # Start indications thread
            log.debug('openolt grpc starting')
            self.indications_thread_handle = threading.Thread(
                target=process_indications,
                args=(self.host_and_port,))
            # self.indications_thread_handle.setDaemon(True)
            self.indications_thread_handle.start()
        except Exception as e:
            log.exception('indication start failed', e=e)
        else:
            log.debug('openolt grpc started')


def process_indications(broker, host_and_port):
    channel = grpc.insecure_channel(host_and_port)
    stub = openolt_pb2_grpc.OpenoltStub(channel)
    stream = stub.EnableIndication(openolt_pb2.Empty())

    default_topic = 'openolt.ind-{}'.format(host_and_port.split(':')[0])
    pktin_topic = 'openolt.pktin-{}'.format(host_and_port.split(':')[0])

    # Producer configuration
    # See https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md
    #
    conf = {'bootstrap.servers': broker}

    # Create Producer instance
    p = Producer(**conf)

    while True:
        try:
            # get the next indication from olt
            print('waiting for indication...')
            ind = next(stream)
        except Exception as e:
            log.warn('openolt grpc connection lost', error=e)
            '''
            ind = openolt_pb2.Indication()
            ind.olt_ind.oper_state = 'down'
            kafka_send_pb(default_topic, ind)
            break
            '''
        else:
            log.debug("openolt grpc rx indication", indication=ind)
            if ind.HasField('pkt_ind'):
                p.produce(pktin_topic,
                          dumps(MessageToJson(
                              ind, including_default_value_fields=True)))
            else:
                p.produce(default_topic,
                          dumps(MessageToJson(
                              ind, including_default_value_fields=True)))


if __name__ == '__main__':
    # pdb.set_trace()

    if len(sys.argv) < 3:
        sys.stderr.write(
            'Usage: %s <kafka-broker> <olt hostname or ip>\n\n' % sys.argv[0])
        sys.exit(1)

    broker = sys.argv[1]
    host = sys.argv[2]

    try:
        # Start indications_process
        log.debug('openolt grpc starting')
        indications_process = Process(
            target=process_indications,
            args=(broker, host,))
        indications_process.start()
    except Exception as e:
        log.exception('indication start failed', e=e)
    else:
        log.debug('openolt grpc started')

    try:
        indications_process.join()
    except KeyboardInterrupt:
        indications_process.terminate()
