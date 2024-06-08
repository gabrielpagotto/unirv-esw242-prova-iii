from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from datetime import timedelta
from leilao.api.models import Item, ItemBid


class ItemBidSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemBid
        fields = "__all__"

    def validate(self, data):
        if data["bid"] <= data["item"].starting_bid:
            raise ValidationError({"error": f"O lance deve ser maior que {data['item'].starting_bid}"})

        item_bids = ItemBid.objects.filter(item=data["item"], bid__gte=data["bid"]).order_by("-bid")[:1]
        if len(item_bids) > 0:
            raise ValidationError({"error": f"O lance deve ser maior que {item_bids[0].bid}"})
        return data


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class ItemRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"

    bids = ItemBidSerializer(many=True, read_only=True)
    days_remaining = serializers.SerializerMethodField(read_only=True)
    highest_bid = serializers.SerializerMethodField(read_only=True)

    def get_days_remaining(self, instance):
        return (instance.created_at + timedelta(days=instance.duration_days) - instance.created_at).days

    def get_highest_bid(self, instance):
        item_bids = ItemBid.objects.filter(item=instance).order_by("-bid")[:1]
        return item_bids[0].bid if len(item_bids) > 0 else instance.starting_bid
