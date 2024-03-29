from django.urls import path
from account import views
from django.contrib.auth import views as auth_views

app_name=  'account'

urlpatterns = [
    path('signup/', views.CreateUser.as_view(), name='sign'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='log'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('get_login/',views.get_login_redirect,name='get_login'),
    path(r'user/(?P<user>[-\w]+)/(?P<pk>\\d+)/',views.UserDetail.as_view(), name='user_detail'),
]
