
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home),
    url(r'^exams/', include('exams.urls')),
    url(r'^results/', include('results.urls')),
    url(r'^companies/', include('companies.urls')),
    url(r'^registration/', include('registration.urls')),
]
