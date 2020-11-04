
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home),
    url(r'^home/$', views.welcome),
     url(r'^account/', include('account.urls')),
    url(r'^exams/', include('exams.urls')),
    url(r'^results/', include('results.urls')),
    url(r'^companies/', include('companies.urls')),
    url(r'^registration/', include('registration.urls')),  
    url(r'^home$',views.home),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)