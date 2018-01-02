from django.contrib import admin

from .models import Course, Carrer, CourseTemplate


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('get_dynamic_natural_key', 'carrer', 'course_template')


@admin.register(CourseTemplate)
class CourseTemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code')


@admin.register(Carrer)
class CarrerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code')
