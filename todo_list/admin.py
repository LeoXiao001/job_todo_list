from django.contrib import admin
from .models import ToDoList, ToDoItem, Profile


@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ['list_name', 'create_date']
    list_filter = ['create_date']


@admin.register(ToDoItem)
class ToDoItem(admin.ModelAdmin):
    list_display = ['item_name', 'priority', 'due_date', 'create_date']
    list_filter = ['priority', 'due_date', 'create_date']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar']