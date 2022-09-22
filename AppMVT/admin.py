from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from . import models




admin.site.register(Coberturasalud)
admin.site.register(Familia)
admin.site.register(Trabajo)
admin.site.register(Autos)


@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'slug', 'author')
    prepopulated_fields = {'slug': ('title',),}

@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'email', 'publish', 'status' )
    list_filter = ('status', 'publish')
    search_fields = ('name', 'email', 'content')


admin.site.register(models.Category)