from django.db import models
from django.utils.text import slugify


class Portfolio(models.Model):

    title = models.CharField(max_length=200)

    slug = models.SlugField(unique=True, blank=True)

    image = models.ImageField(upload_to="portfolio/", blank=True, null=True)

    short_description = models.CharField(max_length=250)

    description = models.TextField()

    project_type = models.CharField(
        max_length=100,
        blank=True,
        help_text="Example: Web Application, E-commerce, API",
    )

    client_name = models.CharField(max_length=150, blank=True)

    technologies = models.CharField(
        max_length=255, help_text="Example: Django, Bootstrap, MySQL"
    )

    github_url = models.URLField(blank=True)

    live_demo = models.URLField(blank=True)

    featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        # Auto-generate unique slug if empty
        if not self.slug:
            base_slug = slugify(self.title) or "project"
            slug = base_slug
            count = 1

            # Loop until a unique slug is found
            while Portfolio.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{count}"
                count += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title