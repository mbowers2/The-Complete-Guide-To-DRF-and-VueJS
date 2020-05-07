from rest_framework import serializers

from jobs.models import Company, JobOffer

class JobOfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobOffer
        exclude = ('id',)

    
class CompanySerializer(serializers.ModelSerializer):
    joboffers = JobOfferSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Company
        fields = '__all__'

