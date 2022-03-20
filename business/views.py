from django.shortcuts import render, redirect
from . models import Business
from .forms import BusinessForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.


def business(request):

    search_querys = ''
    if request.GET.get('search_querys'):
        search_querys = request.GET.get('search_querys')
    
    businesses=Business.objects.filter(
       Q(name__icontains=search_querys)|
       Q(email__icontains=search_querys)
        
    )
    # businesses=Business.objects.all()
    context={'businesses':businesses,"search_querys":search_querys}
    return render(request, 'businesses/business.html', context)



def busines(request,pk):
    businessobj=Business.objects.get(id=pk)
    context={'businessobj':businessobj}
    return render(request, 'businesses/single-business.html', context)



@login_required(login_url='login')
def createBusiness(request):
    form=BusinessForm()
    if request.method=='POST':
        form=BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('business')

    context={'form':form}
    return render(request, 'businesses/business_form.html',context)    



@login_required(login_url='login')
def updateBusines(request,pk):
    business=Business.objects.get(id=pk)
    form=BusinessForm(instance=business)
    if request.method=='POST':
        form=BusinessForm(request.POST,request.FILES, instance=business)
        if form.is_valid():
            form.save()
            return redirect('business')

    context={'form':form}
    return render(request, 'businesses/business_form.html',context)      



@login_required(login_url='login')
def deleteBusines(request,pk):
    business = business.objects.get(id=pk) 
    if request.method=='POST':
        business.delete()
        return redirect('business')
    context={'business':business}
    return render(request,'businesses/business_form.html', context)
