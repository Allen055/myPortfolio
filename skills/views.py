from django.shortcuts import render, redirect, get_object_or_404
from .models import Skill



# PUBLIC VIEW
def skill_list(request):

    skills = Skill.objects.all()

    return render(
        request,
        "skills/skill_list.html",
        {"skills": skills},
    )


# PUBLIC VIEW
def skill_detail(request, pk):

    skill = get_object_or_404(Skill, pk=pk)

    return render(
        request,
        "skills/skill_detail.html",
        {"skill": skill},
    )














