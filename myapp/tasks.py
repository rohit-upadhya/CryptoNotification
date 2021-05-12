from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
import requests
from django.conf import settings
from django.core.mail import send_mail
from datetime import datetime
from pathlib import Path

logger = get_task_logger(__name__)

#image_path = BASE_DIR.joinpath('img.jpeg')

def check_and_send_email():
    response = requests.get('https://api.wazirx.com/api/v2/tickers')
    quotes = response.json()
    d = quotes['dogeinr']
    e = quotes['ethinr']
    eo = quotes['eosinr']
    doge = d['sell']
    doge_buy = ['buy']
    eth = e['sell']
    eos = eo['sell']

    if(float(doge) >= 45.0):
        now = datetime.now()
        subject = f'Quote at { now }'
        message = f'Hi. \n \n Doge is Selling price is at is at { doge }. Time to sell' 
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['rohitupadhya18@gmail.com',]
        send_mail( subject, message, email_from, recipient_list )
    if(float(doge) <= 41.0):
        now = datetime.now()
        subject = f'Quote at { now }'
        message = f'Hi. \n \n Doge is Selling at { doge }. Time to buy' 
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['rohitupadhya18@gmail.com',]
        send_mail( subject, message, email_from, recipient_list )

@periodic_task(
    run_every=(crontab(minute='*/5')),
    name="task_check_API_and_send_emial",
    ignore_result=True
)
def celery_task():
    check_and_send_email()
    logger.info("Sent Emial")
