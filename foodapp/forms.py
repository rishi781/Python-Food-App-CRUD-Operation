from django import forms
from .models import FoodMenu
 
class FoodMenuForm(forms.ModelForm):
    class Meta:
        model = FoodMenu
        fields = ['item_name', 'description', 'price','image_url']