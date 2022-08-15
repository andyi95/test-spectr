from django.urls import include, path
from rest_framework import routers
from api.views import FormViewSet

router = routers.DefaultRouter()

router.register('form', FormViewSet)

urlpatterns = [
    path('', include(router.urls))
]