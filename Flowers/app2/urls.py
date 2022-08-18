'''
Created on 2022. 4. 23.

@author: parlo
'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('app2/', views.page1),
    path('app2/page1', views.page1),
    path('app2/page2', views.page2),
    path('app2/page3', views.page3),
    
]

