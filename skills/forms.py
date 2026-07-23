from django import forms
from .models import Skill


class SkillForm(forms.ModelForm):

    class Meta:

        model = Skill

        fields = "__all__"

        widgets = {

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                }
            ),
        }