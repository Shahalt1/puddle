from django.shortcuts import render, get_object_or_404
from .models import Item

# Create your views here.


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_item = Item.objects.filter(is_sold=False, category=item.category).exclude(
        pk=pk
    )[:3]
    context = {"item": item, "related_item": related_item}
    return render(request, "item/detail.html", context)
