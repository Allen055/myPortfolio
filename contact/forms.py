from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = [
            "name",
            "email",
            "phone",
            "subject",
            "message",
        ]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Gregory Perry"}),
            "email": forms.EmailInput(attrs={"placeholder": "gregoryp@example.com"}),
            "phone": forms.TextInput(attrs={"placeholder": "+234 (80) 0000-00001"}),
            "subject": forms.TextInput(attrs={"placeholder": "Project Inquiry"}),
            "message": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Tell me about your project...",
                }
            ),
        }