from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import MemberList, MemberDetail

app_name = 'member'

urlpatterns = [
    path('members/', MemberList.as_view(), name='list'),
    path('members/<int:pk>/', MemberDetail.as_view(), name='detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
