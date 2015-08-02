__author__ = 'lukas'
from django.conf.urls import url

from .views import SocketRequestHandler

socketRequestHandler=SocketRequestHandler()

urlpatterns = [
    url(r'^$', socketRequestHandler.get_index),
    url(r'^create/$', socketRequestHandler.create_socket),
    url(r'^(?P<socket_id>[0-9]+)/$', socketRequestHandler.get_socket),
    url(r'^(?P<socket_id>[0-9]+)/delete$', socketRequestHandler.delete_socket),
    url(r'^(?P<socket_id>[0-9]+)/send$', socketRequestHandler.send_message),
    url(r'^(?P<socket_id>[0-9]+)/recv$', socketRequestHandler.receiveMessage),
    url(r'^(?P<socket_id>[0-9]+)/settings$', socketRequestHandler.get_socket),
]