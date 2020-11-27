from django.conf.urls import url
from first_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^second/', views.index2, name='index2'),
    url(r'^third/', views.index3, name='index3'),
    url(r'^help/', views.helps, name='helps'),
    url(r'^me/', views.me, name='me')
]
