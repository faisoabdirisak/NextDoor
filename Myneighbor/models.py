import uuid
from django.db import models
from users.models import Profile

# Create your models here.
class Neighbor(models.Model):
    user= models.ForeignKey(Profile,null=True,blank=True,on_delete=models.SET_NULL)
    name=models.CharField(max_length=200)
    location=models.CharField(max_length=200,null=True,blank=True)
    occupation=models.CharField(max_length=200,null=True,blank=True)
    featured_image = models.ImageField(null=True,blank=True, default="default.jpg")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)


    def __str__(self):
        return self.name






class Post(models.Model):
    title=models.CharField(max_length=200)
    post = models.TextField()
    neighbor = models.ForeignKey(Neighbor, on_delete=models.CASCADE, blank=True) 
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False) 



    def __str__(self):
        return self.title