from . import views
from django.urls import path

urlpatterns = [
     path('business/', views.business, name='business'),
    path('busines/<str:pk>', views.busines, name='busines'),

    path('createBusiness/', views.createBusiness, name='createBusiness'),
    path('update-busines/<str:pk>', views.updateBusines, name='update-busines'),

    path('deleteb-busines/<str:pk>', views.deleteBusines, name='delete-busines'),
    ]