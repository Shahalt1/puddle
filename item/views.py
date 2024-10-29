from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Category
from .forms import NewItemForm, EditItemForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.


def items(request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    category_id = request.GET.get("category", 0)
    if category_id:
        items = items.filter(category_id=category_id)
    query = request.GET.get("query", "")
    if query:
        items = Item.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    return render(
        request,
        "item/items.html",
        {
            "items": items,
            "query": query,
            "categories": categories,
            "category_id": int(category_id),
        },
    )


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_item = Item.objects.filter(is_sold=False, category=item.category).exclude(
        pk=pk
    )[:3]
    context = {"item": item, "related_item": related_item}
    return render(request, "item/detail.html", context)


@login_required
def new_item(request):
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect("item:detail", pk=item.id)
    else:
        form = NewItemForm()
    return render(request, "item/form.html", {"form": form, "title": "Add new item"})


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect("dashboard:index")


@login_required
def edit_item(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item.save()
            return redirect("item:detail", pk=item.id)
    else:
        form = EditItemForm(instance=item)
    return render(request, "item/form.html", {"form": form, "title": "Add new item"})
