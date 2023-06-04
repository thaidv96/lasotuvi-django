# from django.conf.urls import url
from django.urls import path, include, re_path


from lasotuvi_django.views import api, lasotuvi_django_index

urlpatterns = [
    re_path(r'^api', api),
    re_path(r'^$', lasotuvi_django_index)
]