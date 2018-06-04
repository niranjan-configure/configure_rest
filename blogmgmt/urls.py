from django.conf.urls import url
import blogapiviews
import imageuploadapiviews
import imageapiviews
import signupapiviews
from rest_framework.authtoken import views

urlpatterns = [ url(r'^api/blogs/(?P<key>[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12})/$',
                    blogapiviews.BlogPostUpdateView.as_view()),
                url(r'^api/blogs/$',blogapiviews.BlogPostView.as_view()),
                url(r'^api/comments/$',blogapiviews.CommentView.as_view()),
                url(r'^api/imageUpload/$', imageuploadapiviews.FileUploadView.as_view()),
                url(r'^api/images/$', imageapiviews.ImageListView.as_view()),
                url(r'^api/likes/$', blogapiviews.LikeView.as_view()),
                url(r'^api/signup/$', signupapiviews.SignupView.as_view()),
                url(r'^api/login/', views.obtain_auth_token),
               ]
