from django.urls import path, include
from rest_framework.routers import DefaultRouter
from leilao.api.views import ItemView, ItemBidView

router = DefaultRouter(trailing_slash="")
router.register(r"items", ItemView)
router.register(r"items-bid", ItemBidView)

urlpatterns = [
    path("", include(router.urls)),
]
