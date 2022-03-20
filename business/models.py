import uuid
from django.db import models
from Myneighbor.models import Neighbor
from users.models import Profile

# Create your models here.
class Business(models.Model):
    user= models.ForeignKey(Profile,null=True,blank=True,on_delete=models.SET_NULL)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    neighbor = models.ForeignKey(Neighbor, on_delete=models.CASCADE, blank=True) 
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False) 


    
    def __str__(self):
        return self.name