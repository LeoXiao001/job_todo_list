from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from .forms import UserRegistrationForm, ListCreateForm, ItemCreateForm
from .models import ToDoList, ToDoItem

# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request,
#                                 username=cd['username'],
#                                 password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('Authenticated successfully')
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid login')
#     else:
#         form = LoginForm()
#
#     return render(request, 'todo_list/login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request,
                'todo_list/dashboard.html',
                {'section': 'dashboard'})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            # user set_password to handle encryption for safety reason
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request,
                        'registration/register_done.html',
                        {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': user_form})


@login_required
def todolist_create(request):
    if request.method == 'POST':
        form = ListCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_list = form.save(commit=False)
            new_list.user = request.user
            new_list.save()
            return redirect('dashboard')
    else:
        form = ListCreateForm()

    return render(request, 'todo_list/create_list.html', {'form': form})


@login_required
def todoitem_create(request, list_id):
    list = ToDoList.objects.get(id=list_id)
    if list in request.user.lists.all():
        if request.method == 'POST':
            form = ItemCreateForm(data=request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                new_item = form.save(commit=False)
                new_item.list = list
                new_item.save()

                # return redirect('dashboard')
                return redirect(list)
        else:
            form = ItemCreateForm()

        return render(request, 'todo_list/create_item.html', {'form': form, 'list': list})

    else:
        return redirect('dashboard')


class TodoitemUpdateView(UpdateView):
    model = ToDoItem
    template_name = 'todo_list/item_update.html'
    fields = ['item_name', 'due_date', 'priority', 'description', 'notification', 'complete']


class TodoitemDeleteView(DeleteView):
    model = ToDoItem
    template_name = 'todo_list/item_confirm_delete.html'

    def get_success_url(self):
        list_id = ToDoItem.objects.get(pk=self.kwargs['pk']).list.id
        return reverse_lazy('list_detail', args=[str(list_id)])


class TodoitemDetailView(DetailView):
    model = ToDoItem
    template_name = 'todo_list/item_detail.html'


class TodolistDetailView(DetailView):
    model = ToDoList
    template_name = 'todo_list/list_detail.html'


class TodolistDeleteView(DeleteView):
    model = ToDoList
    template_name = 'todo_list/list_confirm_delete.html'
    success_url = reverse_lazy('dashboard')


class UserDetailView(DetailView):
    model = User
    template_name = 'todo_list/user_detail.html'

    def get_object(self):
        return self.request.user


class UserUpdateView(UpdateView):
    model = User
    template_name = 'todo_list/user_update.html'
    fields = ['username', 'email']

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('user_detail')
