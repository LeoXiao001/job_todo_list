from django.db import models
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.models import User

import datetime
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFit


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = ProcessedImageField(upload_to='images',
                                format='JPEG',
                                processors=[ResizeToFit(100, 100)],
                                options={'quality': 80})

    @property
    def avatar_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url


class ToDoList(models.Model):
    list_name = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='lists')
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.list_name

    def get_absolute_url(self):
        return reverse('list_detail', args=[str(self.id)])


class ToDoItem(models.Model):
    PRIORITY_CHOICES = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    ]
    item_name = models.CharField(max_length=50)
    create_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=1)
    description = models.TextField()
    list = models.ForeignKey(ToDoList, on_delete=models.CASCADE, related_name='items')
    # notification; if True, send email to notify user
    notification = models.BooleanField(default=False)
    # complete; if True, turn off notification
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse('item_detail', args=[str(self.id)])

    def close_to_due_date(self):
        today = datetime.date.today()
        item_query = ToDoItem.objects.  \
            filter(list__user=self.list.user).  \
            filter(complete=False).  \
            filter(notification=True).  \
            filter(due_date__lte=(today+datetime.timedelta(days=20))).  \
            order_by('due_date', '-priority')

        return item_query
