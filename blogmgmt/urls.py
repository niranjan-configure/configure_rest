from django.conf.urls import url
import blogapiviews
import imageuploadapiviews
import imageapiviews
import signupapiviews
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'^api/blogs', blogapiviews.BlogPostView, base_name="blog" )
router.register(r'^api/comments', blogapiviews.CommentView, base_name="comment" )
router.register(r'^api/images', imageapiviews.ImageListView, base_name="image" )

# URL Patterns not using ViewSet
rem_patterns = [
                url(r'^api/imageUpload/$', imageuploadapiviews.FileUploadView.as_view()),
                url(r'^api/likes/$', blogapiviews.LikeView.as_view()),
                url(r'^api/signup/$', signupapiviews.SignupView.as_view()),
                url(r'^api/login/', views.obtain_auth_token),
               ]

urlpatterns = router.urls + rem_patterns
