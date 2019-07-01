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

log = structlog.get_logger()

class InterfaceInfo(object):
	def __init__(self, host_and_port, intf_id):
		super(InterfaceInfo, self)
		self.host_and_port = host_and_port
		# self.intf_id = (int)(intf_id)

		try:
			self.process = Process(target=self.run, args=((int)(intf_id),))
		except Exception as err:
			log.exception("Failed to initialize interface", e=err)


	def start(self):
		try:
			self.process.start()
		except Exception as err:
			log.exception("Failed to start interface", e=err)

		try:
			self.process.join()
		except KeyboardInterrupt:
			self.process.terminate()

	def run(self, intf_id):
		channel = grpc.insecure_channel(self.host_and_port)
		self.stub = openolt_pb2_grpc.OpenoltStub(channel)
		self.get_status(intf_id)

	def get_status(self, if_id):
		status = self.stub.GetPonIf(openolt_pb2.Interface(intf_id=if_id))
		print('Status is ' + status.oper_state)

if __name__ == '__main__':	
	if len(sys.argv) < 3:
		# Print some kind of error
		sys.exit(1)

	port_and_host = sys.argv[1]
	if_id = sys.argv[2]
	ifinfo = InterfaceInfo(port_and_host, if_id)
	ifinfo.start()

