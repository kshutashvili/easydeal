from django.conf.urls import url

from landing import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^article/(?P<slug>.*)/$', views.article, name='article'),
    url(r'^info/(?P<slug>.*)/$', views.static_page, name='static_page'),
]
