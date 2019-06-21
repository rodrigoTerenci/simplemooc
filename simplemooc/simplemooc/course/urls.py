from django.contrib import admin
from django.urls import path,include, re_path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name='course'

urlpatterns = [
	path('',views.index,name='index'),
	re_path(r'^(?P<slug>[\w_-]+)/$', views.details, name='details'),
] 
