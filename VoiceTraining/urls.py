from django.conf.urls import url
from . import views

urlpatterns =[

    url(r'^voiceUpload$',views.post_new,name='fileUpload')

]
