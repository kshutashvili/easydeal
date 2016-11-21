from django.conf.urls import url
from config import views


urlpatterns = [
    url(r'^currency/$', views.currency, name='set_currency'),
]
