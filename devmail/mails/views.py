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

class MailList(generic.ListView):
    model = models.Mails
    object_name = 'mail_list'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context['now'] = timezone.now()
    #     return context

class MailDetail(generic.DetailView):
    model = models.Mails
    # select_related = ('user', 'group')

    def get_query(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('sender'), pk=self.kwargs.get('pk'))
