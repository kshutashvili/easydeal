from django.conf.urls import url

from catalog import views

urlpatterns = [
    url(r'^detail/(?P<id>\d)/$', views.PropertyDetailView.as_view(), name='detail'),
    url(r'^catalog/$', views.catalog, name='catalog'),
]
