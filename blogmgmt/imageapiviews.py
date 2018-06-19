from rest_framework import serializers, generics, filters, viewsets
from models import Image, ImageComment, ImageLike
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from signupapiviews import UserSerializer

class ImageCommentSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = ImageComment
        fields = ['key','comment_text', 'commented_on','author']

class ImageCommentWriteSerializer(serializers.ModelSerializer):
    image = serializers.SlugRelatedField(
        queryset=Image.objects.all(),
        slug_field='key')
    class Meta:
        model = ImageComment
        fields = ['key','comment_text', 'commented_on', 'image','author']
    def create(self,validated_data):
        validated_data['author'] = self.context['request'].user
        return serializers.ModelSerializer.create(self,validated_data)


class ImageLikeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = ImageLike
        fields = ['key','liked_on','user']

class ImageLikeWriteSerializer(serializers.ModelSerializer):
    image = serializers.SlugRelatedField(
        queryset=Image.objects.all(),
        slug_field='key')
    class Meta:
        model = ImageLike
        fields = ['key', 'liked_on', 'image','user']
    def create(self,validated_data):
        print validated_data
        validated_data['user'] = self.context['request'].user
        return serializers.ModelSerializer.create(self,validated_data)


class ImageSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    comments = ImageCommentSerializer(many=True)
    likes = ImageLikeSerializer(many=True)
    class Meta:
        model = Image
        fields = ['key','location', 'description', 'name','owner','comments','likes', 'uploaded_on']

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

class ImageCommentView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    lookup_field = 'key'
    def get_queryset(self):
        return ImageComment.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST' or self.request.method == 'PUT' or self.request.method == 'PATCH':
            return ImageCommentWriteSerializer
        return ImageCommentSerializer

class ImageLikeView(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ImageLikeSerializer
    def get_queryset(self):
        return ImageLike.objects.all()
    '''
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return LikeWriteSerializer
        return LikeSerializer
    '''
    def post(self, request, *args, **kwargs):
        usr = self.request.user
        if 'post' in request.data:
            image_key = request.data['image']
            like_obj = ImageLike.objects.filter(image__key=image_key, user=usr)
            if like_obj is not None and len(like_obj)>0:
                return Response({"error":"user has already liked the post!"},status = HTTP_400_BAD_REQUEST)
            else:
                like_obj = ImageLike()
                like_obj.user= usr
                like_obj.image = Image.objects.get(key=image_key)
                like_obj.save()
                serializer = ImageLikeSerializer(like_obj)
                return Response(serializer.data,status=HTTP_201_CREATED)
        else:
            return Response({"error":"post key is required!"},status = HTTP_400_BAD_REQUEST)
