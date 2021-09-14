from django.contrib import admin
from django.urls import path
from account.services import UserService
from quickstart_grpc.account_proto import account_pb2_grpc
# from quickstart_grpc.blog_proto import post_pb2_grpc
# from blog.services import PostService
from blog.handlers import grpc_handlers as blog_grpc_handlers

urlpatterns = [
    path('admin/', admin.site.urls),
]


def grpc_handlers(server):
    account_pb2_grpc.add_UserControllerServicer_to_server(UserService.as_servicer(), server)
    blog_grpc_handlers(server)