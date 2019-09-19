from django.urls import path
from . import views

app_name = 'mails'

urlpatterns = [
    # path('',views.MailList.as_view(), name='all'),
    path(r'by/(?P<sender>[-\w]+)/', views.MailList.as_view(), name='all'),
    path(r'by/(?P<sender>[-\w]+)/(?P<pk>\\d+)/', views.MailDetail.as_view(), name='single'),
]
