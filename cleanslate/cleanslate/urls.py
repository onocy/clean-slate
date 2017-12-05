"""cleanslate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from doma.views import home, profile, calendar, reminders, finance, edit_chore_deadline, create_chore, delete_chore, EditUserProfileView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', home, name='doma/login/'),
    url(r'^admin/', admin.site.urls),
    url(r'^doma/$', home, name='doma'),
    url(r'^doma/profile/$', profile, name='profile'),
    url(r'^doma/reminders/$', reminders, name='reminder'),
    url(r'^doma/finance/$', finance, name='finance'),
    url(r'^doma/calendar/$', calendar, name='calendar'),
    url(r'^doma/users/edit/(?P<pk>\d+)/$', EditUserProfileView, name="edit-user-profile"),
    url(r'^doma/chore/(?P<pk>[-\w]+)/edit/$', edit_chore_deadline, name = 'edit-chore-deadline'),
    url(r'^doma/chore/create/$', create_chore, name = 'create-chore'),
    url(r'^doma/chore/(?P<pk>[-\w]+)/delete/$', delete_chore, name = 'delete-chore'),
]

urlpatterns += [
    url(r'^doma/', include('django.contrib.auth.urls')),
]
