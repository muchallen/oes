from django.conf.urls import url
from . import views 

urlpatterns = [
   
    url(r'^$', views.company),
    url(r'viewCompany^$', views.view_company),
    url(r'^addCompany$', views.add_company)
]