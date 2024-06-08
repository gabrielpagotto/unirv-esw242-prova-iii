from rest_framework import viewsets, mixins
from leilao.api.models import Item, ItemBid
from leilao.api.serializers import ItemSerializer, ItemRetrieveSerializer, ItemBidSerializer


class ItemView(viewsets.ModelViewSet):
    queryset = Item.objects.all()

    def get_serializer_class(self):
        return ItemRetrieveSerializer if self.action == "retrieve" else ItemSerializer


class ItemBidView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = ItemBid.objects.all()
    serializer_class = ItemBidSerializer
