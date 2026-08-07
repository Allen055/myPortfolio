from django.shortcuts import get_object_or_404, redirect, render
from .models import Portfolio

# Create your views here.




def portfolio_list(request):
    projects = Portfolio.objects.all()

    return render(
        request,
        "portfolio/portfolio_list.html",
        {"projects": projects},
    )


def portfolio_detail(request, pk):
    project = get_object_or_404(
        Portfolio,
        pk=pk
    )

    return render(
        request,
        "portfolio/portfolio_detail.html",
        {"project": project},
    )











