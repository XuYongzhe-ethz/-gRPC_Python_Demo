# gRPC Python端demo
本demo展示了如何通过gRPC在两个不同的Python进程间传输文件。文件以字节流的形式传输。

Demo的流程为：
1. client端传输DWG文件到server。
2. server读取文件流，并且将dwg文件保存到本地。
3. server将原文件原封不动的传送回client端。
4. client端读取server端的文件流，并且将dwg文件保存到本地。

## 文件夹
    .
    ├── proto                             # gRPC的proto文件
    ├── client_output                     # Demo客户端的输出文件夹
    ├── server_output                     # Demo服务器端端输出文件夹
    ├── testdata                          # 测试输入
    ├── CAD_parser_client.py              # Demo的客户端代码
    ├── CAD_parser_server.py              # Demo的客户端代码
    ├── gRPC_server_template.py           # 模版
 
## 如何运行
我用的 python 3.9.0，其他版本应该也不会有问题。

安装环境

```
python3 -m pip install --upgrade pip 
python3 -m pip install grpcio
python3 -m pip install grpcio-tools
```

生成 proto.py

```
make all
```

运行服务器

```
make run_server
```

运行客户端（在另一个terminal）

```
make run_client
```

## 如何上手
读一遍CAD_parser_client.py和CAD_parser_server.py，然后在gRPC_server_template.py上添加自己的代码。
