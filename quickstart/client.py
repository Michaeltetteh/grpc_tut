import grpc
from quickstart_grpc import account_pb2
from quickstart_grpc import account_pb2_grpc
from google.protobuf.json_format import MessageToJson


with grpc.insecure_channel('localhost:50051') as channel:
    stub = account_pb2_grpc.UserControllerStub(channel)
    #retreive
    # print(stub.Retrieve(account_pb2.UserRetrieveRequest(id=1)))
    print(MessageToJson(stub.Retrieve(account_pb2.UserRetrieveRequest(id=1))))

    # #create
    # print(stub.Create(account_pb2.User(username="test_uasdsaaser",email="test@treassst.test")))
    # print(stub.Create(account_pb2.User(username="test_usdasear",email="test@tsreasst.test")))
    # #detroy
    # print(stub.Destroy(account_pb2.User(id=8)))

    for user in stub.List(account_pb2.UserListRequest()):
        print(MessageToJson(user), end='')


