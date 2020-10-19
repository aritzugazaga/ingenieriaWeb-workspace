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

class Comment(models.Model):
    post = models.ForeignKey(App, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.App.title, self.name)