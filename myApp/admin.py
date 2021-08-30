from django.contrib import admin
from .models import Comment, Photo, Project
# Register your models here.

admin.site.register(Comment)
admin.site.register(Photo)
admin.site.register(Project)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'created_on')
    list_filter = ('created_on')
    search_fields = ('name', 'body')

class ImageInLine(admin.TabularInline):
  model = Photo

class ProjectAdmin(admin.ModelAdmin):
  inlines = [
    ImageInLine
  ]