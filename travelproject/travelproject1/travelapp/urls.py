from django.urls import path
from . import views
urlpatterns=[
    path('',views.demo,name='demo'),
    # path('about/',views.htm,name='htm'),
    # path('contact/',views.funct,name='funct'),
    # path('add/',views.addition,name='addition'),
]