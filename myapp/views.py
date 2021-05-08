from django.shortcuts import render
import requests
from django.conf import settings
from django.core.mail import send_mail
from datetime import datetime


# Create your views here.

def home(request):
    response = requests.get('https://api.wazirx.com/api/v2/tickers')
    quotes = response.json()
    d = quotes['dogeinr']
    e = quotes['ethinr']
    eo = quotes['eosinr']
    doge = d['sell']
    eth = e['sell']
    eos = eo['sell']

    if(float(doge) >= 50.0):
        now = datetime.now()
        subject = f'Quote at { now }'
        message = f'Hi Rohit. \n \n Doge is Selling price is at is at { doge }. Time to sell' 
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['rohitupadhya18@gmail.com', ]
        send_mail( subject, message, email_from, recipient_list )
    if(float(doge) < 45.0):
        now = datetime.now()
        subject = f'Quote at { now }'
        message = f'Hi Rohit. \n \n Doge is Selling price is at is at { doge }. Time to buy' 
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['rohitupadhya18@gmail.com', ]
        send_mail( subject, message, email_from, recipient_list )



    return render(request, 'home.html',{
        'now' : now,
        'doge': quotes['dogeinr']['sell'],
        'eth': quotes['ethinr'],
        'eosinr': quotes['eosinr']
    })