from rest_framework import generics, mixins
from rest_framework import permissions
from rest_framework.exceptions import ValidationError

from ebooks.api.permissions import IsAdminUserOrReadOnly, \
    IsReviewAuthorOrReadOnly
from ebooks.api.pagination import SmallSetPagination
from ebooks.models import Ebook, Review
from ebooks.api.serializers import EbookSerializer, ReviewSerializer

# Concrete class views are generic class views with mixin classes already
# applied to them. These are the views that most applications will use and 
# are built from classes we've already used.
class EbookListCreateAPIView(generics.ListCreateAPIView):
    # queryset order is wanted for pagination so the pagination is consistent
    queryset = Ebook.objects.all().order_by('-id')
    serializer_class = EbookSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # using custom permission class for admin or is read only
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = SmallSetPagination


class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [IsAdminUserOrReadOnly]


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get('ebook_pk')
        ebook = generics.get_object_or_404(Ebook, pk=ebook_pk)
        
        author = self.request.user
        review_queryset = Review.objects.filter(ebook=ebook, author=author)
        if review_queryset.exists():
            raise ValidationError('You have already reviewed the book.')
        
        serializer.save(ebook=ebook, author=author)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]



# class EbookListCreateAPIView(mixins.ListModelMixin, mixins.CreateModelMixin,
#     generics.GenericAPIView):

#     queryset = Ebook.objects.all()
#     serializer_class = EbookSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

    
