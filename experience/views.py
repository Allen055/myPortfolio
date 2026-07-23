from django.shortcuts import render, redirect
from .models import Experience
from .forms import ExperienceForm

# Create your views here.



def experience_list(request):

    experiences = Experience.objects.all()

    return render(
        request,
        "experience/experience_list.html",
        {
            "experiences": experiences
        }
    )



def experience_create(request):

    form = ExperienceForm(
        request.POST or None
    )

    if form.is_valid():
        form.save()
        return redirect(
            "experience:experience_list"
        )


    return render(
        request,
        "experience/experience_form.html",
        {
            "form": form
        }
    )