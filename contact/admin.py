from django.contrib import admin

from .models import Contact

@admin.register(Contact)
class contactadmin(admin.ModelAdmin):
    list_display=['name','phone','email','message']