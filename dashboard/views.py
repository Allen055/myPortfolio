from django.shortcuts import render

from skills.models import Skill
from portfolio.models import Portfolio
from education.models import Education
from experience.models import Experience
from contact.models import ContactMessage
from home.models import Home


def dashboard(request):
    home = Home.objects.first()

    context = {
    "skills_count": Skill.objects.count(),
    "projects_count": Portfolio.objects.count(),
    "education_count": Education.objects.count(),
    "experience_count": Experience.objects.count(),
    "messages_count": ContactMessage.objects.count(),
    "home": home,

   }


    return render(
        request,
        "dashboard/dashboard.html",
        context
    )