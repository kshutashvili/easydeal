from django.conf.urls import url

from catalog import views

urlpatterns = [
    url(r'^catalog/(?P<id>\d+)/$', views.PropertyDetailView.as_view(), name='detail'),
    url(r'^catalog/$', views.catalog, name='catalog'),
]
