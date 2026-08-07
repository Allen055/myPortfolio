from django.contrib import admin
from .models import Education

# Register your models here.


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("school_name", "degree", "field_of_study")
    search_fields = ("school_name", "degree", "field_of_study")