from django.contrib import admin
from .models import Portfolio

# Register your models here.
from django.contrib import admin
from .models import Portfolio


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    # Columns shown in the admin project list
    list_display = ("title", "project_type", "featured", "created_at")

    # Filters on the right sidebar
    list_filter = ("featured", "project_type", "created_at")

    # Search bar across fields
    search_fields = ("title", "description", "technologies", "client_name")

    # Auto-generate the slug as you type the title
    prepopulated_fields = {"slug": ("title",)}

    # Default ordering
    ordering = ("-created_at",)

