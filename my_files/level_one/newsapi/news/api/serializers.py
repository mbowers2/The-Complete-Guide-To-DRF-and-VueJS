from rest_framework import serializers
from django.utils.timesince import timesince
from datetime import datetime

from news.models import Article, Journalist


# class JournalistSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Journalist
#         fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):

    time_since_publication = serializers.SerializerMethodField()
    # Make author show up as author name in json and not pk
    #author = serializers.StringRelatedField()  
    # Use nest model's own serializer for author field
    #author = JournalistSerializer()

    class Meta:
        model = Article
        exclude = ('id',)
        #fields = '__all__' # all fields
        #fields = ('title', 'description', 'body') # some fields

    def get_time_since_publication(self, object):
        '''
        Method to get new serializer method field. The method name is the name
        of the field provided above with get_ prepended to that field name.
        '''
        publication_date = object.publication_date
        now = datetime.now()
        time_delta = timesince(publication_date, now)
        return time_delta

# Can also comment out the author and link things the other way by showing 
# the journalist with the articles as a new field.
class JournalistSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Journalist
        fields = '__all__'

#class ArticleSerializer(serializers.Serializer):
#    id = serializers.IntegerField(read_only=True)
#    author = serializers.CharField()
#    title = serializers.CharField()
#    description = serializers.CharField()
#    body = serializers.CharField()
#    location = serializers.CharField()
#    publication_date = serializers.DateField()
#    active = serializers.BooleanField()
#    created_at = serializers.DateTimeField(read_only=True)
#    updated_at = serializers.DateTimeField(read_only=True)
#
#    def create(self, validated_data):
#        print(validated_data)
#        return Article.objects.create(**validated_data)
#
#    def update(self, instance, validated_data):
#        instance.author = validated_data.get('author', instance.author)
#        instance.title = validated_data.get('title', instance.title)
#        instance.description = validated_data.get('description', instance.description)
#        instance.body = validated_data.get('body', instance.body)
#        instance.location = validated_data.get('location', instance.location)
#        instance.publication_date = validated_data.get('publication_date', instance.publication_date)
#        instance.active = validated_data.get('active', instance.active)
#        
#        # Need to save the model after the changes
#        instance.save()
#
#        return instance
#
#    # Object level
#    def validate(self, data):
#        '''
#        Check that description and title are different.
#        '''
#        if data['title'] == data['description']:
#            raise serializers.ValidationError(
#                'Title and Description must be different!'
#            )
#        return data
#
#    # Field level
#    def validate_title(self, value):
#        if len(value) > 200:
#            reise serializers.ValidationError(
#                'title is too long'
#            )
#        return value
