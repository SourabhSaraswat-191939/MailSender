from django.urls import path, include

from . import views

urlpatterns = [
    path('email_sended', views.send, name='send_email'),
    path('', views.home, name='home'),
]
