from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Blog, Category
from .forms import BlogForm

# Create your views here.



# PUBLIC

def blog_list(request):
    blogs = Blog.objects.filter(
        published=True
    ).order_by("-created_at")

    return render(
        request,
        "blog/blog_list.html",
        {
            "blogs": blogs
        }
    )


def blog_detail(request, slug):
    blog = get_object_or_404(
        Blog,
        slug=slug,
        published=True
    )

    return render(
        request,
        "blog/blog_detail.html",
        {
            "blog": blog
        }
    )


def category_posts(request, slug):
    category = get_object_or_404(
        Category,
        slug=slug
    )

    blogs = Blog.objects.filter(
        category=category,
        published=True
    )

    return render(
        request,
        "blog/category_posts.html",
        {
            "category": category,
            "blogs": blogs
        }
    )


# DASHBOARD

@login_required
def blog_create(request):

    form = BlogForm(
        request.POST or None,
        request.FILES or None
    )

    if form.is_valid():
        form.save()
        return redirect("blog:blog_list")

    return render(
        request,
        "blog/blog_form.html",
        {
            "form": form
        }
    )


@login_required
def blog_update(request, slug):

    blog = get_object_or_404(
        Blog,
        slug=slug
    )

    form = BlogForm(
        request.POST or None,
        request.FILES or None,
        instance=blog
    )

    if form.is_valid():
        form.save()
        return redirect("blog:blog_list")

    return render(
        request,
        "blog/blog_form.html",
        {
            "form": form
        }
    )


@login_required
def blog_delete(request, slug):

    blog = get_object_or_404(
        Blog,
        slug=slug
    )

    if request.method == "POST":
        blog.delete()
        return redirect("blog:blog_list")

    return render(
        request,
        "blog/blog_delete.html",
        {
            "blog": blog
        }
    )