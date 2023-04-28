from django.contrib import admin

# Register your models here.
from .models import blog



@admin.register(blog)
class blogadmin(admin.ModelAdmin):
    list_display=['id','name','date','title','desc','user']