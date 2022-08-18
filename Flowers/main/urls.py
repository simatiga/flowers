'''
Created on 2022. 4. 23.

@author: parlo
'''
from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.index),
    path('main/timeline/', views.timeline),
    # path('', views.test),
    # path('test/', views.test),
    # path('main/contents5.html', TemplateView.as_view(template_name="contents5.html")),
    # path('main/contents', views.contents),
]

