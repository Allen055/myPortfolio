from django.db import models


class Education(models.Model):

    DEGREE_CHOICES = [
        ("Secondary School", "Secondary School"),
        ("Diploma", "Diploma"),
        ("Bachelor", "Bachelor"),
        ("Master", "Master"),
        ("PhD", "PhD"),
        ("Certificate", "Certificate"),
        ("Professional Training", "Professional Training"),
    ]


    school_name = models.CharField(
        max_length=200
    )


    degree = models.CharField(
        max_length=50,
        choices=DEGREE_CHOICES
    )


    field_of_study = models.CharField(
        max_length=200
    )


    start_date = models.DateField()


    end_date = models.DateField(
        blank=True,
        null=True
    )


    currently_studying = models.BooleanField(
        default=False
    )


    grade = models.CharField(
        max_length=50,
        blank=True
    )


    description = models.TextField(
        blank=True
    )


    school_logo = models.ImageField(
        upload_to="education/",
        blank=True,
        null=True
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    class Meta:
        ordering = ["-start_date"]


    def __str__(self):
        return f"{self.school_name} - {self.degree}"