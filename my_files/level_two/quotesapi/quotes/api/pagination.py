from rest_framework.pagination import PageNumberPagination


class QuoteListPagination(PageNumberPagination):
    page_size = 30
