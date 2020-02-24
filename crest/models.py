from django.db import models

# About Model

class About(models.Model):
    description = models.TextField()
    values = models.TextField()
    image = models.ImageField(upload_to="about")

    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"

    def __str__(self):
        return "About us"

# Recent Work Model

class RecentWork(models.Model):
    title = models.CharField(max_length=100, verbose_name="Work title")
    short_description = models.TextField()
    image = models.ImageField(upload_to="works")

    def __str__(self):
        return self.title


