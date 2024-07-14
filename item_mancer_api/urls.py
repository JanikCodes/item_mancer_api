from django.contrib import admin
from django.urls import path
from rest_api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    # test
    path('api/test', ConnectionTestView.as_view(), name="api-conn-test"),
    # auth
    path('api/login', CustomLoginView.as_view(), name="api-login"),
    # item
    path('api/item-overview', ItemUserOverview.as_view(), name="api-item-overview"),
]
