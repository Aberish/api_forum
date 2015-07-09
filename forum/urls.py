from django.conf.urls import patterns, url, include
from forum import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^messages/$', views.MessageList.as_view()),
    url(r'^messages/(?P<pk>[0-9]+)/$', views.MessageDetail.as_view()),
    url(r'^topics/$', views.TopicList.as_view()),
    url(r'^topics/(?P<pk>[0-9]+)/$', views.TopicDetail.as_view()),
    url(r'^categories/$', views.CategoryList.as_view()),
    url(r'^categories/(?P<pk>[0-9]+)/$', views.CategoryDetail.as_view()),
    url(r'^comments/$', views.CommentList.as_view()),
    url(r'^comments/(?P<pk>[0-9]+)/$', views.CommentDetail.as_view()),   
    url(r'^users/$', views.UserProfileList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserProfileDetail.as_view()),
    url(r'^types/$', views.TypeList.as_view()),
    url(r'^types/(?P<pk>[0-9]+)/$', views.TypeDetail.as_view()),         
]
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
urlpatterns = format_suffix_patterns(urlpatterns)