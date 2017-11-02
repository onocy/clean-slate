from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^doma/profile/$', profile, name='profile'),
    url(r'^doma/profile/(?P<username>[\w\-]+)/$',profile, name='profile'),


]
