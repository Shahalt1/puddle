from django import forms
from .models import Item

INPUT_CLASS = "w-full px-6 py-6 rounded-xl border"


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = (
            "category",
            "name",
            "description",
            "image",
            "price",
        )
        widgets = {
            "category": forms.Select(attrs={"class": INPUT_CLASS, "option": "sfdlk"}),
            "name": forms.TextInput(
                attrs={"class": INPUT_CLASS, "placeholder": "Enter item name"}
            ),
            "description": forms.Textarea(
                attrs={"class": INPUT_CLASS, "placeholder": "Enter item description"}
            ),
            "image": forms.FileInput(
                attrs={"class": INPUT_CLASS, "placeholder": "Upload item image"}
            ),
            "price": forms.NumberInput(
                attrs={"class": INPUT_CLASS, "placeholder": "Enter item price"}
            ),
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = (
            "name",
            "description",
            "image",
            "price",
            "is_sold",
        )
        widgets = {
            "name": forms.TextInput(
                attrs={"class": INPUT_CLASS, "placeholder": "Enter item name"}
            ),
            "description": forms.Textarea(
                attrs={"class": INPUT_CLASS, "placeholder": "Enter item description"}
            ),
            "image": forms.FileInput(
                attrs={"class": INPUT_CLASS, "placeholder": "Upload item image"}
            ),
            "price": forms.NumberInput(
                attrs={"class": INPUT_CLASS, "placeholder": "Enter item price"}
            ),
        }
