from django.conf.urls import url
from .. import views

urlpatterns = [
    # url(r'^photo/$', views.photo_list, name='photo_list'),
    url(r'^login/$', views.login_fbv, name='login'),
]
