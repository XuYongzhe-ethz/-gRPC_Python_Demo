import os
import sys
import grpc

import dwgFile_pb2_grpc
import dwgFile_pb2

from concurrent import futures

# gRPC server的类
class CADServicer(dwgFile_pb2_grpc.CADParserServicer):
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
        return dwgFile_pb2.parseCADResult(metadata=dwgFile_pb2.MetaData(
            name=file_name), file=dwgFile_pb2.File(content=file_contents))