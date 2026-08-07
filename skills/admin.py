from django.contrib import admin
from .models import Skill
# Register your models here.

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "level", "percentage", "created_at")
    list_filter = ("level",)
    search_fields = ("name", "description")
