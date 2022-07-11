#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.apps import apps
from django.contrib import admin

# Register your models here.

from app.models import *


class ContactAdmin(admin.ModelAdmin):
    list_filter = []
    search_fields = (
        'id',
    )
    inlines = []
    list_display = ("id", "name", "email", "subject")


admin.site.register(Contact, ContactAdmin)


class ProjectInline(admin.TabularInline):
    model = Project


class CategoryAdmin(admin.ModelAdmin):
    list_filter = []
    search_fields = (
        'id',
    )
    inlines = [ProjectInline]
    list_display = ("id", "name")


admin.site.register(Category, CategoryAdmin)


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage


class ProjectAdmin(admin.ModelAdmin):
    list_filter = []
    search_fields = (
        'id',
    )
    inlines = [ProjectImageInline]
    list_display = ("id", "title", "category", "project_date", "project_url")


admin.site.register(Project, ProjectAdmin)


class ProjectImageAdmin(admin.ModelAdmin):
    list_filter = []
    search_fields = (
        'id',
    )
    inlines = []
    list_display = ("id", "project", "file_url", "is_poster")


admin.site.register(ProjectImage, ProjectImageAdmin)
