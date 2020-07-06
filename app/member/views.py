from rest_framework import viewsets

from .models import Member
from .permissions import APIPermission
from .serializers import MemberSerializer


class MemberViewSet(viewsets.ModelViewSet):
    """
    A model ViewSet for viewing, creating and deleting Member objects.
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [APIPermission]

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
                # For phone numbers to be valid they must have a '+' in front.
                # However, when passing the phone_number through the params the
                # '+' gets removed, so we have to add it back before it gets
                # serialized.
                if allowed_param == 'phone_number':
                    query_value = f'+{query_value[1:]}'

                filter_kwargs = {
                    allowed_param: query_value
                }
                return Member.objects.filter(**filter_kwargs)

        return Member.objects.all()
