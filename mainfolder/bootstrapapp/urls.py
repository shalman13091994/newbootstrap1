from django.urls import path
from .views import home

urlpatterns=[
    path('',home,name='homeee'),
    path('',home,name='indexxx')
]