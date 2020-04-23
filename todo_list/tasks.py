from celery import task
from .emails import send_email_reminder

"""
supervisor will shut down if the website has no traffic,
so the scheduler doesn't work.
Change to use Heroku APScheduler.
"""
# @task()
# def task_send_email_reminder():
#     send_email_reminder()
