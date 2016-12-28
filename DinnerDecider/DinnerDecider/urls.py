"""DinnerDecider URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from account import views as accView
from store import views as stoView
#from store import store_views
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework_swagger.views import get_swagger_view
from django.contrib.auth.models import User
from account.serializers import PasswordSerializer
#from flask import Flask
#from .schema import schema_view


schema_view = get_swagger_view(title='Fxck API')

router = routers.DefaultRouter()
router.register(r'users', accView.UserViewSet)
#router.register(r'login', accView.login)
router.register(r'stores', stoView.StoreViewSet)
router.register(r'storetype', stoView.StoreTypeViewSet)
router.register(r'area', stoView.AreaViewSet)
router.register(r'storephoto', stoView.StorePhotoViewSet)
#router.register(r'stores', store_views.StoreViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^swagger/', schema_view),
    url(r'^docs/', include('rest_framework_docs.urls')),
]
