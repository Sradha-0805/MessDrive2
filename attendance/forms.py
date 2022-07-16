from django import forms
from django.forms import ModelForm
from .models import expense

class ExpenseForm(ModelForm):
    class Meta:
        model = expense
        fields = ('date', 'expense', 'cleaningStaff_per_day', 'cookingStaff_per_day')
    