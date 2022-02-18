from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user import views as user_views
from fileupload import views

router = DefaultRouter()
router.register('users', user_views.UserViewSet, basename='users')


urlpatterns= [
    path('',include(router.urls)),
    path('upload/',views.FileDocumentUpload.as_view(),name='upload'),
]