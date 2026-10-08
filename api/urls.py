from rest_framework.routers import DefaultRouter
from .views import DetailsViewSet , RegisterViewSet
from django.urls import path , include

router = DefaultRouter()
router.register('details', DetailsViewSet)

router2 = DefaultRouter()
router2.register("register", RegisterViewSet)

urlpatterns = [
    path('' , include(router.urls)),
    path('' , include(router2.urls))
]
