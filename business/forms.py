from django.forms import ModelForm
from .models import Business
from django import forms


class BusinessForm(ModelForm):
    class Meta:
        model=Business
        fields='__all__'

        #  widgets ={
        #      ''
        #  }
    def __init__(self, *args,**kwargs):
        super(BusinessForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'un'}) 
