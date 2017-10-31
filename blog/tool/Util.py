from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from myblog.models import Nav, Site
import markdown
from comments.forms import CommentForm
from django.views.generic import ListView, DetailView
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension


def getMarkDown():
    """
    返回markdown实例
    :return:
    """
    md = markdown.Markdown(
        extensions=[
            'markdown.extensions.abbr',
            'markdown.extensions.fenced_code',
            'markdown.extensions.tables',
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            TocExtension(slugify=slugify),
            # 'markdown.extensions.toc',
        ])
    return md


def getNavs():
    """
    按顺序获取导航按钮
    :return:
    """
    return Nav.objects.all().order_by('num')


def getSite():
    """
    获取网站title和关于信息
    :return:
    """
    return Site.objects.first()
