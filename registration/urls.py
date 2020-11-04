from django.conf.urls import url
from . import views 

urlpatterns = [
   
    url(r'^$', views.registration),
     url(r'^addTestee$', views.add_testee)

    
]