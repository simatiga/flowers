'''
Created on 2022. 4. 23.

@author: parlo
'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('app1/', views.page1),
    path('app1/page1_1', views.page1),
    path('app1/page1_2', views.page2),
    path('app1/page1_3', views.page3),
    
]

