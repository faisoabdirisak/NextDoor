from . import views
from django.urls import path

urlpatterns = [
    path('', views.neighbors, name='neighbors'),
    path('neighbor/<str:pk>', views.neighbor, name='neighbor'),

    path('create-neighbor/', views.createNeighbor, name='create-neighbor'),
    path('update-neighbor/<str:pk>', views.updateNeighbor, name='update-neighbor'),

    path('delete-neighbor/<str:pk>', views.deleteNeighbor, name='delete-neighbor'),

   
 
   path('post/', views.post, name='post'),
   path('singlePost/<str:pk>', views.singlePost, name='singlePost'),
   
   path('createPost/<str:pk>', views.createPost, name='createPost'),
   
]