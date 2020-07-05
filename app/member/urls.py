from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import MemberList, MemberDetail

urlpatterns = [
    path('members/', MemberList.as_view()),
    path('members/<int:pk>/', MemberDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
