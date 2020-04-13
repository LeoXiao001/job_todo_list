from celery import task
from .emails import send_email_reminder

@task()
def task_send_email_reminder():
    send_email_reminder()
