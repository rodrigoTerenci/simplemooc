""" 1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))"""

from django.contrib import admin
from django.urls import path, include
from . import views

app_name='core'

urlpatterns = [
	path('', views.home, name='home'),
	path('contato/', views.contact, name='contact'), 
]
