from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', login,
        {'template_name': 'restaurant/login.html'}, name='login'),
    url(r'^logout/$', logout,
        {'template_name': 'restaurant/logout.html'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
]
