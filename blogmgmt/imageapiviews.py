from rest_framework import serializers, generics, filters, viewsets
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
    class Meta:
        model = Image
        fields = ['key','location', 'description', 'name','owner']
    def create(self,validated_data):
        validated_data['owner'] = self.context['request'].user
        return serializers.ModelSerializer.create(self,validated_data)

class ImageListView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    lookup_field = 'key'
    def get_queryset(self):
        return Image.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST' or self.request.method == 'PUT' or self.request.method == 'PATCH':
            return ImageWriteSerializer
        return ImageSerializer
