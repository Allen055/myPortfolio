from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Education
from .forms import EducationForm


# Public Views

def education_list(request):

    educations = Education.objects.all()

    return render(
        request,
        "education/education_list.html",
        {"educations": educations},
    )


def education_detail(request, pk):

    education = get_object_or_404(
        Education,
        pk=pk
    )

    return render(
        request,
        "education/education_detail.html",
        {"education": education},
    )


# Protected Views

@login_required
def education_create(request):

    form = EducationForm(
        request.POST or None,
        request.FILES or None
    )

    if form.is_valid():

        form.save()

        return redirect("education:education_list")

    return render(
        request,
        "education/education_form.html",
        {"form": form},
    )


@login_required
def education_update(request, pk):

    education = get_object_or_404(
        Education,
        pk=pk
    )

    form = EducationForm(
        request.POST or None,
        request.FILES or None,
        instance=education
    )

    if form.is_valid():

        form.save()

        return redirect("education:education_list")

    return render(
        request,
        "education/education_form.html",
        {
            "form": form,
            "education": education,
        },
    )


@login_required
def education_delete(request, pk):

    education = get_object_or_404(
        Education,
        pk=pk
    )

    if request.method == "POST":

        education.delete()

        return redirect("education:education_list")

    return render(
        request,
        "education/education_delete.html",
        {"education": education},
    )