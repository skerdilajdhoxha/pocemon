from django.contrib import admin

from .models import Pokemon


@admin.register(Pokemon)
class BacklinkAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "ability",
    ]
    ordering = ("name",)
    search_fields = ("name", "moves", "ability")
    list_filter = ("moves", "ability")
