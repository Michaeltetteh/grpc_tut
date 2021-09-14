from django.contrib import admin
from django.urls import path
from account.services import UserService
from quickstart_grpc import account_pb2_grpc

urlpatterns = [
    path('admin/', admin.site.urls),
]


def grpc_handlers(server):
    account_pb2_grpc.add_UserControllerServicer_to_server(UserService.as_servicer(), server)