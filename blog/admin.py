from django.contrib import admin
from .models import Blog, Category

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "slug",
    )

    search_fields = (
        "name",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "published",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "published",
        "category",
        "created_at",
    )

    search_fields = (
        "title",
        "summary",
        "content",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    list_editable = (
        "published",
    )

    ordering = (
        "-created_at",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (

        (
            "Blog Information",
            {
                "fields": (
                    "title",
                    "slug",
                    "category",
                    "featured_image",
                )
            },
        ),

        (
            "Content",
            {
                "fields": (
                    "summary",
                    "content",
                )
            },
        ),

        (
            "Publication",
            {
                "fields": (
                    "published",
                )
            },
        ),

        (
            "Dates",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),

    )