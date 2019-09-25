from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.http import Http404
from braces.views import SelectRelatedMixin
from . import models
# from . import forms
from django.contrib.auth import get_user_model
from django.contrib import messages
# Create your views here.


User = get_user_model()

class MailSentList(generic.ListView):
    model = models.Mails
    template_name = 'mails/mails_sent_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(sender__username__iexact=self.kwargs.get('sender'))

class MailReceiveList(generic.ListView):
    model = models.Mails
    template_name = 'mails/mails_receive_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(receiver__username__iexact=self.request.user.username)


class MailDetail(generic.DetailView):
    model = models.Mails
    # select_related = ('user', 'group')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(sender__username__iexact=self.kwargs.get('sender'), pk=self.kwargs.get('pk'))
