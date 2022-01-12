from django.urls import path
from theapi import views
app_name = 'theapi'

urlpatterns = [

    path('', views.home, name='home')

]
