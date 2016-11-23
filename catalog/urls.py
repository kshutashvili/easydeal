from django.conf.urls import url
from .views import DetailView


urlpatterns = [
    url(r'^detail/(?P<id>\d)', DetailView.as_view()),
]
