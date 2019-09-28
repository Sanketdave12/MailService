from django.urls import path
from . import views

app_name = 'mails'

urlpatterns = [
    # path('',views.MailList.as_view(), name='all'),
    path(r'by/(?P<sender>[-\w]+)/', views.MailSentList.as_view(), name='sent'),
    path(r'to/',views.MailReceiveList.as_view(), name='receive' ),
    path(r'by/(?P<sender>[-\w]+)/(?P<pk>\\d+)/', views.MailDetail.as_view(), name='single'),
    path(r'compose/', views.Compose.as_view(), name='compose'),
]
