from django.conf.urls import url

from catalog import views

urlpatterns = [
    url(r'^detail/(?P<id>\d)/$', views.DetailView.as_view(), name='detail'),
    url(r'^$', views.main, name='main'),
    url(r'^catalog/$', views.catalog, name='catalog'),
]
