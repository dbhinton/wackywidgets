from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.widget_create, name='widget_create'),
    path('<int:widget_id>/delete/', views.widget_delete, name='widget_delete')
]