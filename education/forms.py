from django import forms
from .models import Education


class EducationForm(forms.ModelForm):

    class Meta:

        model = Education

        fields = "__all__"

        widgets = {

            "start_date": forms.DateInput(
                attrs={"type": "date"}
            ),

            "end_date": forms.DateInput(
                attrs={"type": "date"}
            ),

            "description": forms.Textarea(
                attrs={"rows":4}
            ),

        }