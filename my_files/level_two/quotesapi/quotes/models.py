from django.db import models

# Create your models here.
class Quote(models.Model):
    author = models.CharField(max_length=120)
    body = models.TextField()
    source = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author}: {self.body[:30]}...'
