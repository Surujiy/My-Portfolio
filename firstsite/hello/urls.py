from django.urls import path
from . import views

app_name = 'cookies'
urlpatterns = [
    path('', views.cookie, name='all')
]
