
from rest_framework import serializers, generics, filters
from models import Comment, Post , Like
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from signupapiviews import UserSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK
from pip._vendor.distro import like


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Comment
        fields = ['key','comment_text', 'commented_on','author']

class CommentWriteSerializer(serializers.ModelSerializer):
    post = serializers.SlugRelatedField(
        queryset=Post.objects.all(),
        slug_field='key')
    class Meta:
        model = Comment
        fields = ['key','comment_text', 'commented_on', 'post','author']
    def create(self,validated_data):
        validated_data['author'] = self.context['request'].user
        return serializers.ModelSerializer.create(self,validated_data)


class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Like
        fields = ['key','liked_on','user']

class LikeWriteSerializer(serializers.ModelSerializer):
    post = serializers.SlugRelatedField(
        queryset=Post.objects.all(),
        slug_field='key')
    class Meta:
        model = Like
        fields = ['key', 'liked_on', 'post','user']
    def create(self,validated_data):
        print validated_data
        validated_data['user'] = self.context['request'].user
        return serializers.ModelSerializer.create(self,validated_data)


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    comments = CommentSerializer(many=True)
    likes = LikeSerializer(many=True)
    class Meta:
        model = Post
        fields = ['key','message', 'posted_on', 'title', 'comments', 'likes', 'author']


class PostWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['key','message', 'posted_on', 'title', 'author']
    def create(self,validated_data):
        validated_data['author'] = self.context['request'].user
        return serializers.ModelSerializer.create(self,validated_data)

class BlogPostView(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get_queryset(self):
        return Post.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PostWriteSerializer
        return PostSerializer

class BlogPostUpdateView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    lookup_field = 'key'
    def get_queryset(self):
        return Post.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH':
            return PostWriteSerializer
        return PostSerializer

class CommentView(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    def get_queryset(self):
        return Comment.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CommentWriteSerializer
        return CommentSerializer

class LikeView(generics.ListCreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = LikeSerializer
    def get_queryset(self):
        return Like.objects.all()
    '''
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return LikeWriteSerializer
        return LikeSerializer
    '''
    def post(self, request, *args, **kwargs):
        usr = self.request.user
        if 'post' in request.data:
            post_key = request.data['post']
            like_obj = Like.objects.filter(post__key=post_key, user=usr)
            if like_obj is not None and len(like_obj)>0:
                return Response({"error":"user has already liked the post!"},status = HTTP_400_BAD_REQUEST)
            else:
                like_obj = Like()
                like_obj.user= usr
                like_obj.post = Post.objects.get(key=post_key)
                like_obj.save()
                serializer = LikeSerializer(like_obj)
                return Response(serializer.data,status=HTTP_201_CREATED)
        else:
            return Response({"error":"post key is required!"},status = HTTP_400_BAD_REQUEST)
