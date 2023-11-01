from django.contrib import admin

from coursesapp import models as coursesapp_models


@admin.register(coursesapp_models.Subject)
class SusjectAdmin(admin.ModelAdmin):
    list_display = ["title", "slug"]
    prepopulated_fields = {"slug": ("title",)}


class ModuleInline(admin.StackedInline):
    model = coursesapp_models.Module


@admin.register(coursesapp_models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["title", "subject", "created"]
    list_filter = ["created", "subject"]
    search_fields = ["title", "overview"]
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ModuleInline]
