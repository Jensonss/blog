from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post, Category, Tag, Nav, Site


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    search_fields = ('title',)
    list_filter = ('category',)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ('name',)


class NavAdmin(admin.ModelAdmin):
    list_display = ['name', 'link', 'num']
    fields = ('name', 'link', 'num',)


class SiteAdmin(admin.ModelAdmin):
    list_display = ['title']
    fields = ('title', 'me',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Nav, NavAdmin)
admin.site.register(Site, SiteAdmin)
