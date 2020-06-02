from django.contrib import admin

# Register your models here.
from .models import Tag, My_post
# admin.site.register(Tag)
# admin.site.register(My_post)

def set_active(modelAdmin, request, queryset):
    queryset.update(is_active = True)

def set_inactive(modelAdmin, request, queryset):
    queryset.update(is_active = False)

class My_postAdmin(admin.ModelAdmin):
    list_display = ['my_post_name', 'my_post_text', 'my_post_rating', 'is_active']
    actions = [set_active, set_inactive]

class TagAdmin(admin.ModelAdmin):
    list_display = ['tag_name', 'is_active']
    actions = [set_active, set_inactive]

admin.site.register(Tag, TagAdmin)
admin.site.register(My_post, My_postAdmin)