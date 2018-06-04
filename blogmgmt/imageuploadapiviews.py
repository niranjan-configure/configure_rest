
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.status import HTTP_201_CREATED
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from signupapiviews import UserSerializer

class FileUploadView(APIView):
    parser_classes = (MultiPartParser, )
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def post(self, request, format='jpg'):
        print request.FILES
        up_file = request.FILES['file']
        destination = open('/home/saba/projects/angular-blog/media-store/' + up_file.name, 'wb+')
        for chunk in up_file.chunks():
            destination.write(chunk)
            destination.close()
        return Response('/media_store/'+up_file.name,  HTTP_201_CREATED)
