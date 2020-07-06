from django.contrib import admin
from django.urls import path, include
from member.views import MemberViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api/member', MemberViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
