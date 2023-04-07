from django.urls import path
from .import views

urlpatterns=[
    path('index',views.home,name='sahad'),
    
    path('livingroom',views.sahad,name='abc'),
    path('bedroom',views.fahim,name='bcd'),
    path('dining',views.rasu,name='cde'),
    path('studyroom',views.shabeer,name='def'),
    path('store',views.shameer,name='efg'),
    path('kitchen',views.musthafa,name='fgh'),


    ]