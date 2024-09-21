from django.urls import re_path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('groups', views.GroupViewSet, basename='groups')

urlpatterns = [
    re_path('login/?$', views.login),
    re_path('logout/?$', views.logout),
    re_path('me/?$', views.me),
    re_path('set-language/?$', views.set_language),
]

urlpatterns += router.urls
