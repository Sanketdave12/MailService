from django.db import models

# Create your models here.
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model
import misaka
# from groups.models import Group

# Create your models here.
User = get_user_model()

class Mails(models.Model):

    sender = models.ForeignKey(User, related_name='mails_sender', on_delete='CASCADE')
    receiver = models.ForeignKey(User, related_name='mails_receiver', on_delete='CASCADE')
    subject = models.TextField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

    def save(self, *args, **kwargs):
        # self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('mails:single', kwargs={
            'sender' : self.sender.username,
            'pk' : self.pk
        })

    class Meta:
        ordering = ['-sent_at']
        unique_together = ['sender', 'subject']
