
from django.conf.urls import include, url
from django.contrib import admin
from django_project.views import home,css

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'^main.css$', css),
]
