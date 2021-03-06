"""practice URL Configuration

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

from count import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^practice/(?P<count_id>\d+)/', views.count_number, name='count'),
    url(r'^reverse/(?P<count_id>\d+)/', views.count_decrease, name='countreverse'),
    url(r'^userdetail/(?P<user_id>\d+)', views.detail, name='userdetail'),
    url(r'^inc_sorting/', views.inc_sorting, name="inc_sorting"),
    url(r'^dec_sorting/', views.dec_sorting, name="dec_sorting"),
    url(r'^arrangement', views.arrangement, name='arrangement'),

]
