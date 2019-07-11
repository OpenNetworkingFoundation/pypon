#  Copyright 2019 Anjali Thontakudi 

#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import sys
import grpc
from multiprocessing import Process
import structlog

import openolt_pb2_grpc
import openolt_pb2

logger = structlog.get_logger()

class OnuInfo(object):
	def __init__(self, host_and_port, intf_id, onu_id):
		super(OnuInfo, self)
		self.host_and_port = host_and_port

		try:
			self.process = Process(target=self.run, args=((int)(intf_id), (int)(onu_id),))
		except Exception as e:
			logger.exception("Failed to initialize ONU", e=e)

	def start(self):
		try:
			self.process.start()
		except Exception as e:
			logger.exception("Failed to start ONU", e=e)

		try:
			self.process.join()
		except KeyboardInterrupt:
			self.process.terminate()

	def run(self, intf_id, onu_id):
		channel = grpc.insecure_channel(self.host_and_port)
		self.stub = openolt_pb2_grpc.OpenoltStub(channel)
		self.get_status(intf_id, onu_id)

	def get_status(self, if_id, onu_id):
		try:
			status = self.stub.GetOnuInfo(openolt_pb2.Onu(intf_id=if_id, onu_id=onu_id))
			print('ONU status is ' + status.oper_state)
		except Exception as e:
			logger.exception('Failed to retrieve ONU status', e=e)

if __name__ == "__main__":
	if(len(sys.argv)<4):
		print('Need all arguments to execute command')
		sys.exit(1)

	port_and_host = sys.argv[1]
	if_id = sys.argv[2]
	onu_id = sys.argv[3]

	OnuInfo(port_and_host, if_id, onu_id).start()
		