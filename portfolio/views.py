from django.shortcuts import get_object_or_404, redirect, render
from .forms import PortfolioForm
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


def portfolio_create(request):

    if request.method == "POST":

        form = PortfolioForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()
            return redirect("portfolio:portfolio_list")

    else:
        form = PortfolioForm()

    return render(
        request,
        "portfolio/portfolio_create.html",
        {"form": form},
    )


def portfolio_update(request, pk):

    project = get_object_or_404(Portfolio,pk=pk)

    if request.method == "POST":

        form = PortfolioForm(
            request.POST,
            request.FILES,
            instance=project,
        )

        if form.is_valid():
            form.save()
            return redirect("portfolio:portfolio_detail", pk=project.pk)

    else:
        form = PortfolioForm(instance=project)

    return render(
        request,
        "portfolio/portfolio_update.html",
        {
            "form": form,
            "project": project,
        },
    )


def portfolio_delete(request, pk):

    project = get_object_or_404(
        Portfolio,
        pk=pk
    )

    if request.method == "POST":
        project.delete()
        return redirect("portfolio:portfolio_list")

    return render(
        request,
        "portfolio/portfolio_delete.html",
        {"project": project},
    )