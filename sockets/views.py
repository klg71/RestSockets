from django.shortcuts import render
from django.http import HttpResponse
from .models import SocketModel
import json
import socket
import hashlib
import time

# Create your views here.
class Socket:
    def __init__(self,address,port,type):
        self.address=address
        self.port=int(port)
        self.type=type
        self.socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def connect(self,name,description):
        self.name=name
        self.description=description
        sha=hashlib.sha1()
        sha.update(self.name)
        sha.update(self.description)
        sha.update(str(time.time()))
        self.accesshash=sha.hexdiges()
        socketModel=SocketModel(self.name,self.description,self.port,self.address,type,self.accesshash)
        socketModel.save()
        self.id=socketModel.id
        self.socket.connect((self.address,self.port))

class SocketRequestHandler:

    def __init__(self):
        self.sockets=[]
        

    def get_index(self,request):
        return HttpResponse(json.dumps({'success':True}))

    def create_scoket(self,request):
        try:
            socket=Socket(request.POST['address'],request.POST['port'])
        except(socket.error) as e:
            return HttpResponse(json.dumps({'success':False,'error':e[1],'errno':e[0]}))
        try:
            socket.connect()
        except(socket.error) as e:
            return HttpResponse(json.dumps({'success':False,'error':e[1],'errno':e[0]}))
        self.sockets.append(socket)
        return HttpResponse(json.dumps({'success':True,'error':None,'errno':None,'id':socket.id,'accesshash':socket.accesshash}))