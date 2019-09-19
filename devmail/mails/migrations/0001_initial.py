# Generated by Django 2.2.1 on 2019-09-19 15:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField()),
                ('message', models.TextField()),
                ('sent_at', models.DateTimeField(auto_now=True)),
                ('receiver', models.ForeignKey(on_delete='CASCADE', related_name='mails_receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete='CASCADE', related_name='mails_sender', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-sent_at'],
                'unique_together': {('sender', 'subject')},
            },
        ),
    ]
