from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register(r'profiles', views.UserProfileViewSet, basename='profiles')

urlpatterns = [
    re_path(r'^hello-view/([0-9]{2})/$', views.HelloApiView.as_view()),
    re_path(r'^login/$', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
