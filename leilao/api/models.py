from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=30, null=False)
    description = models.TextField(null=False)
    starting_bid = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    duration_days = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.description}"


class ItemBid(models.Model):
    bid = models.DecimalField(null=False, max_digits=10, decimal_places=2)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=False, related_name="bids")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.item.name} - {self.bid}"

    class Meta:
        ordering = ["-bid"]
