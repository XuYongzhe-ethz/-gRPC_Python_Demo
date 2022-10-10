import grpc
import dwgFile_pb2
import dwgFile_pb2_grpc


def run():
    f = open("./testdata/test.dwg",'rb+')
    file_content = f.read()
    file_name = "test.dwg"
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = dwgFile_pb2_grpc.CADParserStub(channel)
        file_input = dwgFile_pb2.parseCADRequest(metadata=dwgFile_pb2.MetaData(
            name=file_name), file=dwgFile_pb2.File(content=file_content))
        result = stub.parseCADFile(file_input)
        print(len(result.file.content))
        print(result.metadata.name)

        with open('./output/output.dwg', 'wb') as file:
            file.write(result.file.content)


if __name__ == '__main__':
    run()
