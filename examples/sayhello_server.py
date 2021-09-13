from concurrent import futures
import grpc
from sayhello_pb2 import (RequestMsg, ResponseMsg)
import sayhello_pb2_grpc


class SayHelloService(sayhello_pb2_grpc.SayHelloServicer):

    def SayHello(self, request, context):
        i_d = request.user_id
        return ResponseMsg(id=i_d,title="RECEIVED!")

def serve():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    sayhello_pb2_grpc.add_SayHelloServicer_to_server(

        SayHelloService(), server

    )

    server.add_insecure_port("[::]:50051")

    server.start()

    server.wait_for_termination()



if __name__ == "__main__":
    serve()