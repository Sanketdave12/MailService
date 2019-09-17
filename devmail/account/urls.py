from django.urls import path
from account import views
from django.contrib.auth import views as auth_views

app_name=  'account'

urlpatterns = [
    path('signup/', views.CreateUser.as_view(), name='sign'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='log'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
]
