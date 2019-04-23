
from django.conf.urls import url
from django.urls import include, path
from . import views

urlpatterns = [
    url(r'^', include([
        url(r'^$', views.home, name='tambah'),
        url(r'^home', views.home, name='tambah'),
        url(r'^send', views.send, name='send'),

      
        ])
    )
]