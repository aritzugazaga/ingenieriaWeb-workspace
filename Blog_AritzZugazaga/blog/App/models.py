from django.db import models
from django.urls import reverse

# Create your models here.
class App(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.pk])