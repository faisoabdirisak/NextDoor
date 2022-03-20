from django.forms import ModelForm
from .models import Neighbor, Post
from django import forms

class NeighborForm(ModelForm):
    class Meta:
        model=Neighbor
        fields='__all__'

        #  widgets ={
        #      ''
        #  }
    def __init__(self, *args,**kwargs):
        super(NeighborForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'un'}) 

        # self.fields['name'].widget.attrs.update({'class':'un'})     


class PostForm(ModelForm):
    class Meta:
        model=Post
        fields='__all__'

       
    def __init__(self, *args,**kwargs):
        super(PostForm,self).__init__(*args,**kwargs)

        for title,field in self.fields.items():
            field.widget.attrs.update({'class':'un'}) 

