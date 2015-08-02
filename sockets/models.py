from django.db import models

# Create your models here.
class SocketModel(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=1000)
    port=models.IntegerField()
    address=models.CharField(max_length=100)
    type=models.CharField(max_length=3)
    accesshash=models.CharField(max_length=100)

class MessageModel(models.Model):
    message=models.CharField(max_length=3000)
    socket=models.ForeignKey(SocketModel)