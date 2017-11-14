from django.contrib import admin
from dairy.models import Dairy

# Register your models here.
class DairyAdmin(admin.ModelAdmin):
    list_display = ['body', 'created_time', 'modified_time']
    fields = ('body', 'created_time', 'modified_time',)


admin.site.register(Dairy, DairyAdmin)
