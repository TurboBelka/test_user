from django.urls import re_path

from . import views

app_name = "index"

urlpatterns = [
    re_path(r'^$', views.UsersView.as_view(), name='index'),
    re_path(r'^login', views.block_login_page, name='login'),
    re_path(r'^logout', views.user_logout, name='logout'),
    re_path(r'^loggedin', views.get_current_user, name='loggedin'),
    re_path(r'^registration', views.register_user, name='registration'),
    re_path(r'^profile', views.profile, name='profile'),
]