from django import forms
from .models import Portfolio


class PortfolioForm(forms.ModelForm):

    class Meta:
        model = Portfolio

        fields = [
            "title",
            "image",
            "short_description",
            "description",
            "technologies",
            "github_url",
            "live_demo",
            "featured",
        ]

        widgets = {
            "description": forms.Textarea(
                attrs={"rows": 5}
            ),
        }