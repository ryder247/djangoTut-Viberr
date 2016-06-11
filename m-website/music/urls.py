from django.conf.urls import include, url
from . import views

urlpatterns = [
    #/music/ ---> main page
    url(r'^$', views.index, name='index'),

    #/music/42/ ---> details page
     url(r'^(?P<album_id>[0-9]+)$', views.detail, name='detail'),

]
