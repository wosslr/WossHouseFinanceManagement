"""HouseFinanceManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from housefinance import views
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'accounts', views.AccountViewSet)

urlpatterns = [
    url(r'^restapi/', include(router.urls)),
    url(r'^ffm/', include('housefinance.urls', namespace='ffm')),
    url(r'^account/', include('account.urls', namespace='account')),
    url(r'^', include('account.urls', namespace='account')),
    url(r'^wechat/', include('wechat.urls', namespace='wechat')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^api-token-auth/', obtain_auth_token),
]
