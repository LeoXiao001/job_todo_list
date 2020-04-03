from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.urls import reverse
import datetime

from .models import ToDoItem


def send_email_reminder():
    today = datetime.date.today()
    users = User.objects.all()
    from_email = settings.EMAIL_HOST_USER
    for user in users:
        query = ToDoItem.objects.  \
            filter(list__user=user).  \
            filter(complete=False).  \
            filter(notification=True).  \
            filter(due_date__lte=(today+datetime.timedelta(days=20))).  \
            order_by('due_date', '-priority')

        if not query:
            continue

        to_email = [user.email]
        # body = 'Hi {},\n\n'.format(user.username)
        if len(query) > 1:
            subject = '{} job todo items are due soon'.format(len(query))
            # body += 'You have {} items are due soon. '.format(len(query))
        else:
            subject = '1 job todo item is due soon'
            # body += 'You have 1 item is due soon. '
        # body += 'You can click here({}) to login your dashboard.\n\n'.format(reverse('dashboard'))

        # for item in query:
        #     body += 'List Name: {}\n'.format(item.list.list_name)
        #     body += 'Item name: {}\n'.format(item.item_name)
        #     body += 'priority: {}\tdue date: {}\n'.format(item.get_priority_display(), item.due_date)
        #     body += 'description: {}\n\n'.format(item.description)
        msg_html = render_to_string('todo_list/email.html',
                                    {
                                        'username': user.username,
                                        'query': query,
                                    })
        email = EmailMessage(
            subject=subject,
            body=msg_html,
            from_email=from_email,
            to=to_email,
        )
        email.content_subtype = 'html'
        email.send(fail_silently=False)
