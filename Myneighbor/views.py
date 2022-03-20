from django.shortcuts import render, redirect
from . models import Neighbor, Post
from .forms import NeighborForm,PostForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def neighbors(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    neighbors=Neighbor.objects.filter(
       Q(name__icontains=search_query)|
       Q(location__icontains=search_query)
        
    )
    # neighbors=Neighbor.objects.all()
    context={'neighbors':neighbors, "search_query":search_query}
    return render(request, 'neighbours/neighbors.html', context)

def neighbor(request,pk):
    neighborobj=Neighbor.objects.get(id=pk)
    context={'neighborobj':neighborobj}
    return render(request, 'neighbours/neighbor.html', context)


@login_required(login_url='login')
def createNeighbor(request):
    form=NeighborForm()
    if request.method=='POST':
        form=NeighborForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('neighbors')

    context={'form':form}
    return render(request, 'neighbours/neighbor_form.html',context)    

@login_required(login_url='login')
def updateNeighbor(request,pk):
    neighbor=Neighbor.objects.get(id=pk)
    form=NeighborForm(instance=neighbor)
    if request.method=='POST':
        form=NeighborForm(request.POST,request.FILES, instance=neighbor)
        if form.is_valid():
            form.save()
            return redirect('neighbors')

    context={'form':form}
    return render(request, 'neighbours/neighbor_form.html',context)        

@login_required(login_url='login')
def deleteNeighbor(request,pk):
    neighbor = Neighbor.objects.get(id=pk) 
    if request.method=='POST':
        neighbor.delete()
        return redirect('neighbors')
    context={'neighbor':neighbor}
    return render(request,'neighbours/delete.html', context)    

# posts

def post(request):
    posts=Post.objects.all()
    context={'posts':posts}
    return render(request, 'posts/post.html', context) 


@login_required(login_url='login')
def createPost(request):
    form=PostForm()
    if request.method=='POST':
        form=PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post')

    context={'form':form}
    return render(request, 'posts/post_form.html',context)

def singlePost(request,pk):
    postobj=Post.objects.get(id=pk)
    context={'postobj':postobj}
    return render(request, 'posts/single-post.html', context)

