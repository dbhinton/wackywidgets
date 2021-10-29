from django.forms import ModelForm
from .models import Widget
from django import forms

class WidgetForm(ModelForm):
    class Meta:
        model = Widget
        fields = ['description', 'quantity']