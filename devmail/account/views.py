from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth import get_user_model
from . import forms
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Create your views here.

User = get_user_model()

class UserList(ListView):

    model = User
    template_name = 'mail_data.html'

class CreateUser(CreateView):

    form_class = forms.UserCreateForm

    success_url = reverse_lazy('account:log')
    template_name = 'account/signup.html'

class LogInUser(CreateView):
    pass
