from django.db import models
from user.models import User


class Item(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField()

    class Meta:
        db_table = "items"

class Shop(models.Model):
    name = models.CharField(max_length=100)
    items = models.ManyToManyField(Item, related_name="shops")
    user = models.ForeignKey(User, related_name="shops", on_delete=models.CASCADE)

    class Meta:
        db_table = "shops"

class Chart(models.Model):
    user = models.OneToOneField(User, related_name="chart", on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, related_name="chart")

    class Meta:
        db_table = "charts"

