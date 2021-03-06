"""LightDQM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, patterns, include
from .views import BugListView, BugDetailView, RegisterView, BugCreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib import admin
from LightDQM.views import *
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^help/', dqm_help),
    url(r'^dqm_canvases/', dqm_canvases),
    url(r'^all_plots/$', all_plots),
    url(r'^all_plots/chip/$', chip_plots),
    url(r'^main/$', main),
    url(r'^main/chamber/$', chamber),
    url(r'^chamber/chip/$', chamber),
    url(r'^run/chamber/$', chamber),
    url(r'^main/([a-zA-Z]+)/run/(\d+)/$', chamber),
    url(r'^main/([a-zA-Z]+)/run/(\d+)/([\w\+%_&\- ]+)/$', chamber_tabs),

#for bugtracker
    url(r'^bugs/', include('bugtracker.urls')),
]
