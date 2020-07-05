from rest_framework import generics
from rest_framework import mixins

from .models import Member
from .serializers import MemberSerializer
from .permissions import APIPermission


class MemberList(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):
    """
    List all members, or create a new member.
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [APIPermission]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        """
        Optionally restricts the returned member based on the URL query
        parameter.

        Note: Return all the members if query_param passed is not one of the
        allowed query params.
        """
        allowed_query_params = [
            'id', 'account_id', 'phone_number', 'client_member_id'
        ]
        for allowed_param in allowed_query_params:
            query_value = self.request.query_params.get(allowed_param, None)
            if query_value is not None:
                filter_kwargs = {
                    allowed_param: query_value
                }
                return Member.objects.filter(**filter_kwargs)

        return Member.objects.all()


class MemberDetail(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   generics.GenericAPIView):
    """
    Retrieve or update a member instance.
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [APIPermission]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
