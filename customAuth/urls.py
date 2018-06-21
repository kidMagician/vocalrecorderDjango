from django.conf.urls import url
from .views import *
from rest_framework.authtoken import views

urlpatterns = [

        url(r'^join$',JoinCUser.as_view(),name="join"),
        url(r'^login$',views.obtain_auth_token,name="login"),
        url(r'^findPass$',FIndPass.as_view(),name="findPass"),

]