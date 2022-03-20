# from distutils.command.upload import upload
# import email
# from email.policy import default
# from unicodedata import name
import email
import uuid
from django.db import models
from django.contrib.auth.models import User

# from django.db.models.signals import post_save,post_delete
# from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,blank=True,null=True)
    email=models.EmailField(max_length=500,null=True,blank=True)
    profile_image=models.ImageField(null=True,blank=True,upload_to='profiles/', default="default.jpg")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False) 

    def __str__(self):
        return str(self.name)

# @receiver(post_save, sender=Profile)
# def createProfile(sender,instance,created,**kwargs):
#     if created:
#         user=instance
#         profile=Profile.objects.create(
#             user=user,
#             email=user.email,
#             name=user.username,
          
#         )


# def deleteUser(sender,instance,**kwargs):
#     user=instance.user
#     user.delete()
    

# post_save.connect(createProfile, sender=User)   
# post_delete.connect(deleteUser,sender=Profile)     