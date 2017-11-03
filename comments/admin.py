from django.contrib import admin
from .models import Comment


# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'text', 'created_time','cid','pid','rid']
    fields = ('name', 'text','pid','rid')


admin.site.register(Comment, CommentAdmin)
