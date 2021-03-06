from cProfile import label
from django.forms  import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreation(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        labels={
            
        }


    def __init__(self, *args,**kwargs):
        super(CustomUserCreation,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'un'})     