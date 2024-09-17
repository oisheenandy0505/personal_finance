# finance/urls.py
from django.urls import path
from .views import home, save_entry

urlpatterns = [
    path('', home, name='home'),
    path('save-entry', save_entry, name='save_entry'),
]
