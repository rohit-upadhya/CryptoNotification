from typing import ContextManager
from django.shortcuts import render
import requests
from django.conf import settings
from django.core.mail import send_mail
from datetime import datetime
from .forms import CryptoForm
from .models import Crypto
import json

# Create your views here.

def home(request):
    response = requests.get('https://api.wazirx.com/api/v2/tickers')
    quotes = response.json()
    doge = quotes['dogeinr']
    eth = quotes['ethinr']
    eos = quotes['eosinr']
    doge_sell = doge['sell']
    eth_sell = eth['sell']
    eos_sell = eos['sell']
    now = datetime.now()
    new_var = 'email'
    all_records = list(Crypto.objects.values_list(new_var, flat=True))[0]
    #item = all_records.get('email')
    jsonString = json.dumps(all_records)


    return render(request, 'home.html',{
        'now' : now,
        'doge': doge_sell,
        'eth': eth_sell,
        'eosinr': eos_sell,
        'all': all_records
    })

def detailed_quotes(request):
    context = {}
    form = CryptoForm(request.POST)

    if form.is_valid():
        form.save()

    context['form'] = form

    return render(request, 'registration/profile.html', context)
