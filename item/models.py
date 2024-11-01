from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name


class Item(models.Model):
    class Meta:
        ordering = ("name",)
        verbose_name_plural = "Items"

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to="item_images", blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="items", on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, related_name="items", on_delete=models.CASCADE, default=None
    )

    def __str__(self):
        return self.name
