from django.conf.urls import url
from . import views

app_name = 'usuarios'
urlpatterns = [
    url(r'^$', views.home, name = "home"),
    url(r'^login/$', views.login_view, name = "login"),
    url(r'^logout/$', views.logout_view, name = "logout"),
    url(r'^registrar/$', views.RegistrationView.as_view(), name = "registrar"),
    url(r'^pesquisar/$', views.search_view, name = "pesquisar"),
]