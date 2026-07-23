from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.

def contact_view(request):
    form = ContactForm(
        request.POST or None
    )

    if form.is_valid():
        form.save()
        return redirect(
            "contact:contact_success"
        )

    return render(
        request,
        "contact/contact.html",
        {
            "form": form
        }
    )


def contact_success(request):
    return render(
        request,
        "contact/contact_success.html"
    )


from .models import ContactMessage


def message_list(request):
    messages = ContactMessage.objects.all()

    return render(
        request,
        "contact/message_list.html",
        {
            "messages": messages
        }
    )