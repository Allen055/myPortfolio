from django.shortcuts import render


def about(request):
    return render(request, "about/about.html")


def story(request):
    return render(request, "about/story.html")


def mission(request):
    return render(request, "about/mission.html")