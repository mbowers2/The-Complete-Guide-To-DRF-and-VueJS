from django.urls import path

from jobs.api.views import JobOfferListCreateAPIView, JobOfferDetailAPIView, \
    CompanyListCreateAPIView, CompanyDetailAPIView


urlpatterns = [
    path(
        'jobs/',
        JobOfferListCreateAPIView.as_view(),
        name='job_list',
    ),
    path(
        'jobs/<int:pk>/',
        JobOfferDetailAPIView.as_view(),
        name='job_detail',
    ),
    path(
        'company/',
        CompanyListCreateAPIView.as_view(),
        name='company_list',
    ),
    path(
        'company/<int:pk>',
        CompanyDetailAPIView.as_view(),
        name='company_detail',
    ),
]