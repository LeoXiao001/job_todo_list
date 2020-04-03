# from celery.task.schedules import crontab
# from celery.decorators import periodic_task
# from celery.utils.log import get_task_logger
#
# from .emails import send_email_reminder
#
#
# logger = get_task_logger(__name__)
#
# @periodic_task(
#     # run_every=(crontab(hour=5, minute=30)),
#     run_every=(crontab(minute='*/1')),
#     name="task_send_email_reminder",
#     ignore_result=True
# )
# def task_send_email_reminder():
#     send_email_reminder()
#     # print('hello')
#     logger.info("Send job todo item reminder by email")


# from __future__ import absolute_import, unicode_literals
#
from celery import task
from .emails import send_email_reminder

@task()
def task_send_email_reminder():
    send_email_reminder()


# from celery import shared_task
#
# from .emails import send_email_reminder
#
# @shared_task
# def task_send_email_reminder():
#     send_email_reminder()
