from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # test
    path('api/test', ConnectionTestView.as_view(), name="api-conn-test"),
    # auth
    path('api/login', CustomLoginView.as_view(), name="api-login"),
    
]
