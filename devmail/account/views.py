from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth import get_user_model
from . import forms
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views import generic
from . import models

# Create your views here.
from mails import views
User = get_user_model()

class UserList(ListView):

    model = User
    template_name = 'mail_data.html'

class CreateUser(CreateView):

    form_class = forms.UserCreateForm

    success_url = reverse_lazy('account:log')
    template_name = 'account/signup.html'

class LogInUser(CreateView):
    success_url = reverse_lazy('account:log')

def get_login_redirect(request):
    return views.MailReceiveList.as_view()(request)

class UserDetail(generic.ListView):
    model = User
    template_name = 'account/user_detail.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(username=self.request.user.username)
