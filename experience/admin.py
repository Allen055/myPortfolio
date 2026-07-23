from django.contrib import admin
from .models import Experience

# Register your models here.



@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):

    list_display = (
        "position",
        "company",
        "start_date",
        "end_date",
        "current_job",
    )

    list_filter = (
        "current_job",
    )