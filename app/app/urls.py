from django.contrib import admin
from django.urls import path, include
from member.views import MemberViewSet
from rest_framework.routers import DefaultRouter
from fileuploader.views import csv_upload

router = DefaultRouter()
router.register('members', MemberViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', csv_upload, name="profile_upload"),
]
