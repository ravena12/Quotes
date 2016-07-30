from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name = 'my_quote_index'),
    url(r'^register/$', views.register, name = 'my_quote_register'),
    url(r'^login/$', views.processlogin, name = 'my_quote_login'),
    url(r'^logout/$', views.logout, name = 'my_quote_logout'),
    url(r'^process/$', views.processregister, name = 'my_register_process'),
    url(r'^home/$', views.home, name = 'my_quote_home'),
    url(r'^create/$', views.processquote, name = 'my_quote_add'),
    url(r'^createproduct/$', views.createproduct, name = 'my_quote_addpage'),
    url(r'^product/(?P<id>\d+)$', views.product, name = 'my_quote_product'),
    url(r'^join/(?P<id>\d+)$', views.join, name = 'my_quote_join'),
    url(r'^destroy/(?P<id>\d+)$', views.destroy, name = 'my_quote_destroy'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name = 'my_quote_delete'),
]

