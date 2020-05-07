from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()

    def __str__(self):
        return self.name


class JobOffer(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='joboffers'
    )
    job_title = models.CharField(max_length=120)
    job_description = models.TextField()
    salary = models.SmallIntegerField()
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.company.name}: {self.job_title}'



