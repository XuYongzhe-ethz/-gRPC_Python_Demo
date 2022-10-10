import os
import sys
import grpc

import dwgFile_pb2_grpc
import dwgFile_pb2

from concurrent import futures


class CADServicer(dwgFile_pb2_grpc.CADParserServicer):
    def parseCADFile(self, request, context):
        print("file received..")
        file_contents = request.file.content
        file_name = request.metadata.name
        print("received new file, ", file_name,
              ", file size: ", len(file_contents))
        with open('./server_output/output.dwg', 'wb') as file:
            file.write(request.file.content)

        return dwgFile_pb2.parseCADResult(metadata=dwgFile_pb2.MetaData(
            name=file_name), file=dwgFile_pb2.File(content=file_contents))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dwgFile_pb2_grpc.add_CADParserServicer_to_server(
        CADServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("CAD parser is listening in port 50051")
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
