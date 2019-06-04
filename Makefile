#  Copyright 2019 Shad Ansari
#
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

help:
	@echo "Usage: make [<target>]"
	@echo "where available targets are:"
	@echo
	@echo "protos       : Compile all grpc/protobuf files"
	@echo "clean        : Remove files created by the build and tests"
	@echo "help         : Print this help"
	@echo

protos:
	make -C protos

install-protoc:
	make -C protos install-protoc

clean:
	find . -name '*.pyc' | xargs rm -f


protos-clean:
	find openoltd -name '*pb2.py' | xargs rm -f
	find openoltd -name '*pb2_grpc.py' | xargs rm -f

.PHONY: protos
