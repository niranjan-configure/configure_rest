from rest_framework import serializers, generics, filters
from models import Image
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from signupapiviews import UserSerializer

class ImageSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    class Meta:
        model = Image
        fields = ['key','location', 'description', 'name','owner']

class ImageWriteSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    class Meta:
        model = Image
        fields = ['key','location', 'description', 'name','owner']
    def create(self,validated_data):
        validated_data['owner'] = self.context['request'].user
        return serializers.ModelSerializer.create(self,validated_data)

class ImageListView(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get_queryset(self):
        return Image.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ImageWriteSerializer
        return ImageSerializer
