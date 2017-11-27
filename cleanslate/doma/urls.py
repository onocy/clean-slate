from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^chore/(?P<pk>[-\w]+)/edit/$', views.edit_chore_deadline, name = 'edit-chore-deadline'),
]
