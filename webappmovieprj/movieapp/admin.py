from django.contrib import admin
from . models import Category,Movie
# Register your models here.
class categoryadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,categoryadmin)

class movieadmin(admin.ModelAdmin):
    list_display = ['name','desc','cast','trailer','rel_date','category','image','created','updated']
    list_editable = ['desc','cast','trailer','rel_date','category','image']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
admin.site.register(Movie, movieadmin)