from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^button/$', views.buttonpage, name='buttonpage'),
    url(r'^form/$', views.formpage, name='formpage'),
    url(r'^record/$', views.recordpage, name='recordpage'),


    #AJAX creation methods
    url(r'^create_record/$', views.create_record, name="create_record"),

    #AJAX deletion methods
    url(r'^delete_record/(?P<pk>\d+)/$', views.delete_record, name="delete_record"),

    #AJAX return record methods
    url(r'^list_record/all$', views.list_records, name="list_records"),
    url(r'^list_record/latest/$', views.list_latest_record, name="list_latest_record"),
    url(r'^list_record/(?P<pk>\d+)/$', views.list_single_record, name="list_single_record"),

    #AJAX return methods
    url(r'^random_word/$', views.random_word, name="random_word"),
    url(r'^random_int/$', views.random_int, name="random_int"),
    url(r'^random_int/(?P<max_range>\d+)$', views.random_int, name="random_int"),
]