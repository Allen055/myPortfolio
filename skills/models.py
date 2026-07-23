
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Skill(models.Model):

    LEVELS = [
        ("Beginner", "Beginner"),
        ("Intermediate", "Intermediate"),
        ("Advanced", "Advanced"),
        ("Expert", "Expert"),
    ]


    name = models.CharField(
        max_length=100
    )


    level = models.CharField(
        max_length=20,
        choices=LEVELS,
        default="Beginner"
    )


    percentage = models.PositiveIntegerField(
        default=80,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )


    icon = models.ImageField(
        upload_to="skills/",
        blank=True,
        null=True
    )


    description = models.TextField(
        blank=True
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    class Meta:
        ordering = ["name"]


    def __str__(self):
        return self.name