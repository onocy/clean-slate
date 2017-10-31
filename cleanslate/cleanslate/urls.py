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
from doma.views import home, profile, calendar, reminders, finance

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^doma/$', home, name='doma'),
    url(r'^$', home, name='doma'),
    url(r'^doma/profile/$', profile, name='profile'),
    url(r'^doma/reminders/$', reminders, name='reminder'),
    url(r'^doma/finance/$', finance, name='finance'),
    url(r'^doma/calendar/$', calendar, name='calendar'),
]



# urlpatterns += [
#         url(r'^home/', include('cleanslate.urls')),
# ]
#
# urlpatterns += [
#         url(r'^$', RedirectView.as_view(url='/doma/', permanent=True)),
# ]
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
