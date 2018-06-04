from rest_framework import serializers
from django.contrib.auth.models import User, Group, Permission
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.response import Response
from rest_framework.authtoken import views

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name','email']

class SignupView(APIView):
    def post(self, request):
        parsed_data = request.data
        if "username" not in parsed_data:
            return Response({"error":"username required!"},  HTTP_400_BAD_REQUEST)
        if "password" not in parsed_data:
            return Response({"error":"password required!"},  HTTP_400_BAD_REQUEST)

        user_name = parsed_data['username']
        password = parsed_data['password']

        user_obj = User.objects.filter(username=user_name)
        if user_obj is not None and len(user_obj)>0:
            return Response({"error":"Username already exists!"},  HTTP_400_BAD_REQUEST)
        else:
            usr=User.objects.create_user(user_name, email=user_name,  password=password)
            usr.first_name = ''
            usr.last_name = ''
            usr.save()
            token, created = Token.objects.get_or_create(user=usr)
            data = {'token':token.key}
            return Response(data,status=HTTP_201_CREATED)
