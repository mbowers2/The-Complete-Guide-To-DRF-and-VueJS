from django.contrib import admin

from jobs.models import Company, JobOffer


# Register your models here.
admin.site.register(Company)
admin.site.register(JobOffer)
