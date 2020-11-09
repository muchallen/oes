from django.conf.urls import url
from . import views

app_name='account'

urlpatterns =[
    url(r'^signup/$', views.signup_view, name='signup'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^forget/$', views.forget_view, name='forget'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^accounts/$', views.all_users, name='all-users'),
    url(r'^my_account/$', views.my_account, name='my-users'),
    
]