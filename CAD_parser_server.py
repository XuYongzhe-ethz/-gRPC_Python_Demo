import os
import sys
import grpc

import gRPCFileParser_pb2_grpc
import gRPCFileParser_pb2

from concurrent import futures

# gRPC server的类
class CADServicer(gRPCFileParser_pb2_grpc.gRPCFileParserServicer):
    # 从客户端读取DWG文件，存储在本地，并且原封不动的返回DWG文件
    def parseCADFile(self, request, context):
        print("file received..")
        file_contents = request.file.content
        file_name = request.metadata.name
        print("received new file, ", file_name,
              ", file size: ", len(file_contents))
        with open('./server_output/output.dwg', 'wb') as file:
            file.write(request.file.content)

        # 返回原本的DWG文件
        return gRPCFileParser_pb2.parseCADResult(metadata=gRPCFileParser_pb2.MetaData(
            name=file_name), file=gRPCFileParser_pb2.File(content=file_contents))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    gRPCFileParser_pb2_grpc.add_gRPCFileParserServicer_to_server(
        CADServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("CAD parser is listening in port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
