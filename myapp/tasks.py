from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
import requests
from django.conf import settings
from django.core.mail import send_mail
from datetime import datetime
from pathlib import Path
from .models import Crypto

logger = get_task_logger(__name__)

#image_path = BASE_DIR.joinpath('img.jpeg')

def check_and_send_email():
    response = requests.get('https://api.wazirx.com/api/v2/tickers')
    quotes = response.json()

    now = datetime.now()
    all_records = list(Crypto.objects.values())
    




@periodic_task(
    run_every=(crontab(minute='*/5')),
    name="task_check_API_and_send_emial",
    ignore_result=True
)
def celery_task():
    check_and_send_email()
    logger.info("Sent Emial")
