# 自定义模板标签
from ..models import Post, Category,Tag
from django import template
from django.db.models.aggregates import Count

register = template.Library()


# 注意 Django 1.9 后才支持 simple_tag 模板标签，如果你使用的 Django 版本小于 1.9，你将得到一个错误。Django 1.9 以前的版本如何自定义模板标签这里不再赘述。
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    # 别忘了在顶部引入 Category 类
    # return Category.objects.all()
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)


@register.simple_tag
def get_tags():
    # 记得在顶部引入 Tag model
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
