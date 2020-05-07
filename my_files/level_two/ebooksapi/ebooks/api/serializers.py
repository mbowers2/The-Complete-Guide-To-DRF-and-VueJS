from rest_framework import serializers

from ebooks.models import Ebook, Review


class ReviewSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        # Need to exclude ebook from the serializer since it is added to the
        # serializer in the views.ReviewCreateAPIView.perform_create method,
        # where the ebook is added to the serializer.
        exclude = ('ebook',)
        #fields = '__all__'


class EbookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Ebook
        fields = '__all__'

