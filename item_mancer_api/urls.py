from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_api.views import *

router = DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'rarities', RarityViewSet)

urlpatterns = [
    # test
    path('api/test/', ConnectionTestView.as_view(), name="api-conn-test"),
    # auth
    path('api/login/', CustomLoginView.as_view(), name="api-login"),
    # item
    path('api/item-overview/', ItemUserOverview.as_view(), name="api-item-overview"),
    # rarity
    path('api/rarity-overview/', RarityUserOverview.as_view(), name="api-rarity-overview"),
    
    path('api/', include(router.urls)),
]
