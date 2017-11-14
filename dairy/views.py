from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
import markdown
from comments.forms import CommentForm
from django.views.generic import ListView, DetailView
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from dairy.models import Dairy
from blog.tool import Util
# Create your views here.
app_name = 'dairy'


class IndexView(ListView):
    model = Dairy
    template_name = app_name + '/dairy.html'
    context_object_name = 'dairy_list'
    # 分页，每页数量
    paginate_by = 10

    def get_queryset(self):
        return super(IndexView, self).get_queryset().order_by('-created_time')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        md = Util.getMarkDown()
        site = Util.getSite()
        site.me = md.convert(site.me)
        context.update({
            'navs': Util.getNavs(),
            'site': site,
        })
        return context