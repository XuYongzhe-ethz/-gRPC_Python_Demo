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
        # 这里是接收到的文件都字节流
        file_contents = request.file.content

        # 接收到的文件的文件名
        file_name = request.metadata.name

        # --------------------------------------------------
        #                  添加自己的逻辑代码  
        # --------------------------------------------------
        # ...

        # --------------------------------------------------
        #                  替换以下的变量
        # --------------------------------------------------
        # 最终文件的内容
        final_file_content = bytearray([1,2,3,4,5,6,7,8,9,10])

        # 文件名
        name = "this_is_a_test"

        # 文件类型
        file_type = "txt"

        # 返回结果
        return gRPCFileParser_pb2.parseCADResult(metadata=gRPCFileParser_pb2.MetaData(
            name=file_name, type=file_type), file=gRPCFileParser_pb2.File(content=final_file_content))

# 开启服务器
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
