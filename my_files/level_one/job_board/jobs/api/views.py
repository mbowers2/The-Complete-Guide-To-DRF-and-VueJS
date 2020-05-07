from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from jobs.models import JobOffer, Company
from jobs.api.serializers import JobOfferSerializer, CompanySerializer

class JobOfferListCreateAPIView(APIView):

    def get(self, request):
        jobs = JobOffer.objects.filter(active=True)
        # Set many=True since articles is a QuerySet of mulitiple articles
        serializer = JobOfferSerializer(jobs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = JobOfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class JobOfferDetailAPIView(APIView):

    def get_object(self, pk):
        job = get_object_or_404(JobOffer, pk=pk)
        return job

    def get(self, request, pk):
        job = self.get_object(pk)
        serializer = JobOfferSerializer(job)
        return Response(serializer.data)

    def put(self, request, pk):
        job = self.get_object(pk)
        serializer = JobOfferSerializer(job, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        job = self.get_object(pk)
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CompanyListCreateAPIView(APIView):

    def get(self, request):
        companies = Company.objects.all()
        # Set many=True since articles is a QuerySet of mulitiple articles
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class CompanyDetailAPIView(APIView):

    def get_object(self, pk):
        company = get_object_or_404(Company, pk=pk)
        return company

    def get(self, request, pk):
        company = self.get_object(pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    def put(self, request, pk):
        company = self.get_object(pk)
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        company = self.get_object(pk)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
