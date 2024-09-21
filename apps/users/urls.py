from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path('login/?$', views.login),
    re_path('logout/?$', views.logout),
    re_path('me/?$', views.me),
    re_path('set-language/?$', views.set_language),
]
