from django.contrib import admin
from .models import ToDoList, ToDoItem


@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ['list_name', 'create_date']
    list_filter = ['create_date']


@admin.register(ToDoItem)
class ToDoItem(admin.ModelAdmin):
    list_display = ['item_name', 'priority', 'due_date', 'create_date']
    list_filter = ['priority', 'due_date', 'create_date']
