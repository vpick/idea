from django.conf.urls import url

from . import views

urlpatterns=[
    #url(r'^$',views.index, name='index'),
    url(r'^$',views.member_list, name='member_list'),
    url(r'^contact/$',views.new_member,name='new_member'),
    url(r'^detail/(?P<pk>\d+)/$', views.member_detail, name='member_detail'),
    url(r'^member-info/$', views.display_member, name='display_member'),
    ]