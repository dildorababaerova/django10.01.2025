from django.contrib import admin

from .models import Homepage, EmailPage


@admin.register(Homepage)
class HomepageAdmin(admin.ModelAdmin):
    list_display = ["text", "date"]


@admin.register(EmailPage)
class EmailPageAdmin(admin.ModelAdmin):
    list_display = ["email", "date"]
