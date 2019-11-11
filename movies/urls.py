from django.conf.urls import url
from .views import *

app_name = 'api'

urlpatterns = [
    url(r'^movies', IndexView.as_view(), name='index')
]