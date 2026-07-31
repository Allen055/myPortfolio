from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Skill
from .forms import SkillForm


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


# PRIVATE (Dashboard/Admin only)
@login_required
def skill_create(request):

    form = SkillForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect("skills:skill_list")

    return render(request, "skills/skill_form.html", {"form": form})


# PRIVATE
@login_required
def skill_update(request, pk):

    skill = get_object_or_404(Skill, pk=pk)

    form = SkillForm(
        request.POST or None,
        request.FILES or None,
        instance=skill,
    )

    if form.is_valid():
        form.save()
        return redirect("skills:skill_list")

    return render(request, "skills/skill_form.html", {"form": form})


# PRIVATE
@login_required
def skill_delete(request, pk):
    skill = get_object_or_404(Skill, pk=pk)

    if request.method == "POST":
        skill.delete()
        return redirect("skills:skill_list")
    return render(request, "skills/sill_delete.html", {"skill": skill})






