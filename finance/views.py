# In your views.py
from django.http import JsonResponse
from django.shortcuts import render
from .models import Entry  # Make sure you have an Entry model

def home(request):
    return render(request, 'finance/home.html')

def save_entry(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        credit_debit = request.POST.get('credit_debit')
        category = request.POST.get('category')
        # Create a new entry in the database
        entry = Entry.objects.create(name=name, amount=amount, credit_debit=credit_debit, category=category)
        return JsonResponse({'success': True, 'entry': {
            'name': entry.name,
            'amount': entry.amount,
            'credit_debit': entry.credit_debit,
            'category': entry.category
        }})
    return JsonResponse({'success': False})

