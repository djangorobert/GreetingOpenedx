from django.db import models

# Create your models here.


class Greeting(models.Model):
    post = models.CharField(max_length=150)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp', ]

    def __str__(self):
        return self.post
