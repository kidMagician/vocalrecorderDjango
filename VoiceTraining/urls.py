from django.conf.urls import url
from . import views

urlpatterns =[

    url(r'^voiceUpload$',views.getTrainigVoice,name='voiceUpload'),
    url(r'^homeworkvoiceUpload$', views.homeworkVoiceUP, name='homeworkVoiceUpload'),
    url(r'^searchTeacher$', views.searchTeacher, name='searchTeacher'),
    url(r'^feedBack$',views.sendFeedback,name='sendFeedBack'),
    url(r'^post$',views.post,name='post')

]
