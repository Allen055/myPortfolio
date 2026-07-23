from django.db import models

# Create your models here.

class Home(models.Model):
    full_name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    short_bio = models.TextField()

    hero_image = models.ImageField(
        upload_to='home/',
        blank=True,
        null=True
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    location = models.CharField(
        max_length=100,
        blank=True
    )

    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)

    resume = models.FileField(
        upload_to='resume/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Page"

    def __str__(self):
        return self.full_name