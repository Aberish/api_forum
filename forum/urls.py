from django.conf.urls import patterns, url, include
from forum import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^messages/$', views.MessageList.as_view()),
    url(r'^messages/(?P<pk>[0-9]+)/$', views.MessageDetail.as_view()),
]
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
urlpatterns = format_suffix_patterns(urlpatterns)