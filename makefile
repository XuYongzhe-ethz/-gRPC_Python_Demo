all:
	@python3 -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/gRPCFileParser.proto

run_server:
	@python3 CAD_parser_server.py

run_client:
	@python3 CAD_parser_client.py

clean:
	@rm -rf server_output/*
	@rm -rf client_output/*
	@rm *pb2*.py