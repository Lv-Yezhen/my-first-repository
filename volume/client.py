import grpc
from pubsub_pb2 import mes2client, mes2server
from pubsub_pb2_grpc import pubsubStub
#这里的ip地址要改成server的地址
with grpc.insecure_channel('172.17.0.4:50000') as channel:
	stub = pubsubStub(channel)
	mes = stub.pubsubServe(mes2server(mes1='client'), timeout=500)
	print(mes)
	 
	