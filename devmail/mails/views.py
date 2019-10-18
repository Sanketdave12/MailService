from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.http import Http404
from braces.views import SelectRelatedMixin
from . import models
# from . import forms
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.http import HttpResponseRedirect
from . import forms

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

class Compose(generic.CreateView):
    form_class = forms.ComposeForm
    model = models.Mails
    template_name = 'mails/compose.html'
    # widgets = {'receiver': forms.TextInput}


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.sender = self.request.user
        self.object.save()
        return super().form_valid(form)


class Search(generic.ListView):
    model = models.Mails
    template_name = 'mails/mails_search.html'
    # subject = 'test3'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(receiver__username__iexact=self.request.user.username)
        if not self.request.GET.get('search'):
            return queryset
        queryset = queryset.filter(subject__icontains=self.request.GET.get('search'))
        return queryset
