from django import forms
from .models import Product,Review

class ProductForm(forms.ModelForm):
    class Meta:
        model= Product
        fields = ['category','name','description','image']






