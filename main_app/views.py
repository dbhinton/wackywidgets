from django.shortcuts import render, redirect
from .models import Widget
from .forms import WidgetForm
# Create your views here.

def home(request):
    widgets = Widget.objects.all()
    widget_form = WidgetForm()
    total = 0
    for widget in widgets:
        total += widget.quantity
    return render(request, 'home.html', {'widgets': widgets, 'widget_form': widget_form, 'total': total})

def widget_create(request):
    form = WidgetForm(request.POST)
    if form.is_valid():
        add_widget = form.save(commit=False)
        add_widget.save()

    return redirect('home')

def widget_delete(request, widget_id):
    Widget.objects.filter(id=widget_id).delete()
    return redirect('home')



