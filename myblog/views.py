from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Tag, Nav, Site
import markdown
from comments.forms import CommentForm
from django.views.generic import ListView, DetailView
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from blog.tool import Util
from django.db.models import Q

app_name = 'myblog'

def vpn(request,param):
    """
    vpn页面
    :param request:
    :return:
    """
    return render(request, app_name + '/vpn.html', {'navs': Util.getNavs(),
                                                      'site': Util.getSite()})
class AboutView(ListView):
    model = Nav
    template_name = app_name + '/about.html'

    def get_queryset(self):
        return super(AboutView, self).get_queryset()

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        md = Util.getMarkDown()
        site = Util.getSite()
        site.me = md.convert(site.me)
        context.update({
            'navs': Util.getNavs(),
            'site': site,
        })
        return context


class IndexView(ListView):
    model = Post
    template_name = app_name + '/index.html'
    context_object_name = 'post_list'
    # 分页，每页数量
    paginate_by = 10

    def get_queryset(self):
        return super(IndexView, self).get_queryset().order_by('-created_time')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        site = Util.getSite()
        context.update({
            'navs': Util.getNavs(),
            'site': site,
        })
        return context


class CategoryView(ListView):
    model = Post
    template_name = app_name + '/index.html'
    context_object_name = 'post_list'
    paginate_by = 10

    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate).order_by('-created_time')

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        site = Util.getSite()
        context.update({
            'navs': Util.getNavs(),
            'site': site,
        })
        return context


class TagView(ListView):
    model = Post
    template_name = app_name + '/index.html'
    context_object_name = 'post_list'
    paginate_by = 10

    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagView, self).get_queryset().filter(tags=tag).order_by('-created_time')

    def get_context_data(self, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        site = Util.getSite()
        context.update({
            'navs': Util.getNavs(),
            'site': site,
        })
        return context


class ArchiveView(ListView):
    model = Post
    template_name = app_name + '/index.html'
    context_object_name = 'post_list'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ArchiveView, self).get_context_data(**kwargs)
        site = Util.getSite()
        context.update({
            'navs': Util.getNavs(),
            'site': site,

        })
        return context

    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super(ArchiveView, self).get_queryset().filter(created_time__year=year,
                                                              created_time__month=month).order_by('-created_time')


class PostDetailView(DetailView):
    # 这些属性的含义和 ListView 是一样的
    model = Post
    template_name = app_name + '/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        # 覆写 get 方法的目的是因为每当文章被访问一次，就得将文章阅读量 +1
        # get 方法返回的是一个 HttpResponse 实例
        # 之所以需要先调用父类的 get 方法，是因为只有当 get 方法被调用后，
        # 才有 self.object 属性，其值为 Post 模型实例，即被访问的文章 post
        response = super(PostDetailView, self).get(request, *args, **kwargs)

        # 将文章阅读量 +1
        # 注意 self.object 的值就是被访问的文章 post
        self.object.increase_views()

        # 视图必须返回一个 HttpResponse 对象
        return response

    def get_object(self, queryset=None):
        # 覆写 get_object 方法的目的是因为需要对 post 的 body 值进行渲染
        post = super(PostDetailView, self).get_object(queryset=None)
        md = Util.getMarkDown()
        post.body = md.convert(post.body)
        post.toc = md.toc;
        return post

    def get_context_data(self, **kwargs):
        # 覆写 get_context_data 的目的是因为除了将 post 传递给模板外（DetailView 已经帮我们完成），
        # 还要把评论表单、post 下的评论列表传递给模板。
        context = super(PostDetailView, self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        site = Util.getSite()
        context.update({
            'navs': Util.getNavs(),
            'form': form,
            'comment_list': comment_list,
            'site': site,

        })
        return context





def search(request):
    """
    关键词搜索
    :param request:
    :return:
    """
    key = request.GET.get('key')
    error_msg = ''

    if not key:
        error_msg = "请输入关键词"
        return render(request, app_name + '/index.html', {'navs': Util.getNavs(),
                                                          'site': Util.getSite(),
                                                          'error_msg': error_msg})

    post_list = Post.objects.filter(Q(title__icontains=key) | Q(body__icontains=key))
    return render(request, app_name + '/index.html', {'navs': Util.getNavs(),
                                                      'site': Util.getSite(),
                                                      'error_msg': error_msg,
                                                      'post_list': post_list})


def index(request):
    # return HttpResponse("欢迎访问我的博客首页！")
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, app_name + "/index.html",
                  context={'post_list': post_list})


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # 阅读量 +1
    post.increase_views()
    # 记得在顶部引入 markdown 模块
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])

    # 记得在顶部导入 CommentForm
    form = CommentForm()
    # 获取这篇 post 下的全部评论
    comment_list = post.comment_set.all()

    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, app_name + '/detail.html', context=context)


def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    ).order_by('-created_time')
    return render(request, app_name + '/index.html', context={'post_list': post_list})


def category(request, pk):
    # 记得在开始部分导入 Category 类
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, app_name + '/index.html', context={'post_list': post_list})
