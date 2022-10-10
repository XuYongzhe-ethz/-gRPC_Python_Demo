import grpc
import gRPCFileParser_pb2
import gRPCFileParser_pb2_grpc


def run():
    # 打开测试输入
    f = open("./testdata/test.dwg",'rb+')
    file_content = f.read()
    file_name = "test.dwg"
    
    # 远程调用gRPC函数
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = gRPCFileParser_pb2_grpc.gRPCFileParserStub(channel)

        # 准备函数的para
        file_input = gRPCFileParser_pb2.parseCADRequest(metadata=gRPCFileParser_pb2.MetaData(
            name=file_name), file=gRPCFileParser_pb2.File(content=file_content))

        # 远程调用server函数
        result = stub.parseCADFile(file_input)

        # debug
        print(len(result.file.content))
        print(result.metadata.name)

        # 存储server返回的文件
        with open('./client_output/output.dwg', 'wb') as file:
            file.write(result.file.content)

if __name__ == '__main__':
    run()
