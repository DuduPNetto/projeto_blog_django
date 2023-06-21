from typing import Any

from blog import models
from django.contrib import admin
from django.http.request import HttpRequest
from django_summernote.admin import SummernoteModelAdmin


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug',)
    list_display_links = ('name',)
    search_fields = ('id', 'name', 'slug',)
    list_per_page = 10
    ordering = ('-id',)
    prepopulated_fields = {
        "slug": ('name',)
    }

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug',)
    list_display_links = ('name',)
    search_fields = ('id', 'name', 'slug',)
    list_per_page = 10
    ordering = ('-id',)
    prepopulated_fields = {
        "slug": ('name',)
    }

@admin.register(models.Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published',)
    list_display_links = ('title',)
    search_fields = ('id', 'title', 'slug', 'content')
    list_per_page = 10
    list_filter = ('is_published',)
    list_editable = ('is_published',)
    ordering = ('-id',)
    prepopulated_fields = {
        "slug": ('title',)
    }

@admin.register(models.Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('id', 'title', 'is_published',)
    list_display_links = ('title',)
    search_fields = ('id', 'title', 'slug', 'content', 'excerpt', 'cover',)
    list_per_page = 50
    list_filter = ('category', 'is_published',)
    list_editable = ('is_published',)
    ordering = ('-id',)
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by',)
    prepopulated_fields = {
        "slug": ('title',)
    }
    autocomplete_fields = ('tags', 'category',)

    def save_model(self, request: HttpRequest, obj: Any, form: Any, change: Any) -> None:
        if change:
            obj.updated_by = request.user
        else:
            obj.created_by = request.user
        obj.save()