import grpc
from quickstart_grpc.account_proto import account_pb2
from quickstart_grpc.account_proto import account_pb2_grpc
from google.protobuf.json_format import MessageToJson
from quickstart_grpc.blog_proto import post_pb2, post_pb2_grpc


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

    post_stub = post_pb2_grpc.PostControllerStub(channel)
    print('----- Create -----')
    response = post_stub.Create(post_pb2.Post(title='t1', content='c1'))
    print((MessageToJson(response)), end='')
    print('----- List -----')
    for post in post_stub.List(post_pb2.PostListRequest()):
        print(MessageToJson(post), end='')
    print('----- Retrieve -----')
    response = post_stub.Retrieve(post_pb2.PostRetrieveRequest(id=response.id))
    print(MessageToJson(response), end='')
    print('----- Update -----')
    response = post_stub.Update(post_pb2.Post(id=response.id, title='t2', content='c2'))
    print(MessageToJson(response), end='')
    
    print('----- Delete -----')
    post_stub.Destroy(post_pb2.Post(id=response.id))
    