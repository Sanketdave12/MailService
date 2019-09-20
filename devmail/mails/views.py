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

    def get_query(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('sender'))

class MailDetail(generic.DetailView):
    model = models.Mails
    # select_related = ('user', 'group')

    def get_query(self):
        try:
            self.account_user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
             raise Http404
        else:
            return self.post_user.posts.all()
