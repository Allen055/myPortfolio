from django.shortcuts import render, redirect, get_object_or_404
from .models import Education



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

