from django.conf.urls import url
from .views import *

urlpatterns = [
    url('index', jsonvalid.as_view()),
]