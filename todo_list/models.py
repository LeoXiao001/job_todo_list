from django.db import models
from django.conf import settings
from django.urls import reverse

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
