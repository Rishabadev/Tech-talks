from django import forms
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class ProductForm(forms.ModelForm):

    class Meta:
        model= Product
        fields = ['category','name','brand','description','price','image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'price': forms.NumberInput(attrs={'step': '0.01'}),
        }


class AdminRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True  
        if commit:
            user.save()
        return user
      

