from django.conf.urls import url
from  myblog import views as blogView
from comments import views as commentView

urlpatterns = [
    url(r'^$', blogView.IndexView.as_view(), name='index'),
    url(r'^index$', blogView.IndexView.as_view(), name='index'),
    url(r'^index.html$', blogView.IndexView.as_view(), name='index'),
    url(r'^tag/(?P<pk>[0-9]+)/$', blogView.TagView.as_view(), name='tag'),
    url(r'^post/(?P<pk>[0-9]+)/$', blogView.PostDetailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', blogView.ArchiveView.as_view(), name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', blogView.CategoryView.as_view(), name='category'),
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', commentView.post_comment, name='post_comment'),
    url(r'^search$', blogView.search, name='search'),
    url(r'^vpn(.html)?$', blogView.vpn, name='vpn'),

]
