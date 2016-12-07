from django.conf.urls import url

from landing import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^info/(?P<slug>.*)/$', views.static_page, name='static_page'),
]
