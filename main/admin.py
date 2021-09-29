from django.contrib import admin

from main.models import TestModel


@admin.register(TestModel)
class TestModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
