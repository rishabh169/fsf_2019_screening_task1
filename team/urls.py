from django.conf.urls import url
from . import views

app_name = 'task'

urlpatterns = [
    url(r'^$', views.task_list, name="list"),
    url(r'^create/$', views.task_create, name="create"),
    url(r'^(?P<slug>[\w-]+)/$', views.task_detail, name="detail"),
]
