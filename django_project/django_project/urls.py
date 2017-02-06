
from django.conf.urls import include, url
from django.contrib import admin
from django_project.views import hello,css

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', hello),
    url(r'^main.css$', css),
]
