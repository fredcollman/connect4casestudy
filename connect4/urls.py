from django.conf.urls import url
from connect4 import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^games/$', views.games, name='games'),
    url(r'^games/(\d+)/$', views.games, name='games'),
    url(r'^play/(\d+)/$', views.play, name='play'),
    url(r'^$', views.games, name='home'),
]
