from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from Authentication.views import LoginPage


urlpatterns=[
    path('',views.LoginPage.as_view(),name="loginPage"),
]