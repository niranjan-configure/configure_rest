from django.conf.urls import patterns, url, include
from django.contrib import admin
from learn.views import IndexView
from boards import views

urlpatterns = patterns(
    '',

   url(r'^$', views.home, name='home'),
   url(r'^blogs/', views.home, name='home'),
   url(r'^api/getblogs/', views.get_blog, name='allblogs'),
    url(r'^api/newtopic/', views.get_add_new_topic, name='addnewtopic'),
   url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
   url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),

   url(r'^blogmgmt/',include('blogmgmt.urls')),
  
   url(r'^admin/', admin.site.urls),
)
