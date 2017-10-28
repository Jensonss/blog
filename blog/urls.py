"""untitled1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from  myblog import views as blogView
from comments import views as commentView
from myblog.feeds import AllPostsRssFeed
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', blogView.IndexView.as_view(), name='index'),
    url(r'^tag/(?P<pk>[0-9]+)/$', blogView.TagView.as_view(), name='tag'),
    url(r'^post/(?P<pk>[0-9]+)/$', blogView.PostDetailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', blogView.ArchiveView.as_view(), name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', blogView.CategoryView.as_view(), name='category'),
    url(r'^comment/post/(?P<post_pk>[0-9]+)/$', commentView.post_comment, name='post_comment'),
    url(r'^all/rss/$', AllPostsRssFeed(), name='rss'),
]
