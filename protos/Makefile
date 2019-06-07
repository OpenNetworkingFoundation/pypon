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

default: build

PROTO_FILES := $(wildcard *.proto)
PROTO_PB2_FILES := $(foreach f,$(PROTO_FILES),$(subst .proto,_pb2.py,$(f)))
PROTO_PB2_GPRC_FILES := $(foreach f,$(PROTO_FILES),$(subst .proto,_pb2_grpc.py,$(f)))
PROTO_DESC_FILES := $(foreach f,$(PROTO_FILES),$(subst .proto,.desc,$(f)))

PROTOC_LIBDIR := /usr/local/lib

build: protos

protos: $(PROTO_PB2_FILES)

%_pb2.py: %.proto Makefile
	@echo "Building protocol buffer artifacts from $<"
	env LD_LIBRARY_PATH=$(PROTOC_LIBDIR) python -m grpc.tools.protoc \
	    -I. \
	    --python_out=../ponster \
	    --grpc_python_out=../ponster \
	    $<

clean:
	rm -f $(PROTO_PB2_FILES) $(PROTO_PB2_GPRC_FILES) $(PROTO_DESC_FILES)
