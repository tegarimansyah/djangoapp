"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from health_check.views import MainView
from apps.fake.views import delay, random, setversion

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("django_prometheus.urls")),
    path("health/", MainView.as_view(), name="health_check_custom"),
    url(r"^delay/$", delay, name="delay"),
    url(r"^random/$", random, name="random"),
    url(r"^setversion/$", setversion, name="setversion"),
]
