from django.db import models


class Experience(models.Model):

    company = models.CharField(
        max_length=200
    )

    position = models.CharField(
        max_length=200
    )

    employment_type = models.CharField(
        max_length=100,
        blank=True
    )

    description = models.TextField()

    start_date = models.DateField()

    end_date = models.DateField(
        blank=True,
        null=True
    )

    current_job = models.BooleanField(
        default=False
    )


    class Meta:
        ordering = ["-start_date"]


    def __str__(self):
        return f"{self.position} at {self.company}"