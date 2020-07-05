from django.test import TestCase
from django.urls import reverse
from member.models import Member
from rest_framework import status
from rest_framework.test import APIClient

MEMBER_URL = reverse('member:list')


class MemberApiViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.member = Member.objects.create_dummy_member()

    ###########################################################################
    # GET
    ###########################################################################

    def test_get_member_list(self):
        """Test making GET request to get all members."""
        res = self.client.get(MEMBER_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data[0]['id'], self.member.id)
        self.assertEqual(len(res.data), 1)

    def test_get_member_list_with_params(self):
        """
        Test making GET request with params.

        This should return a queryset of all of the records that match this
        params.
        """
        res = self.client.get(f'{MEMBER_URL}?phone_number=+15555555555')

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        response_member = res.data[0]
        self.assertEqual(response_member['id'], self.member.id)
        self.assertEqual(response_member['first_name'], self.member.first_name)
        self.assertEqual(response_member['last_name'], self.member.last_name)
        self.assertEqual(
            int(response_member['account_id']), self.member.account_id.id
        )
        self.assertEqual(
            response_member['client_member_id'], self.member.client_member_id
        )
        self.assertEqual(len(res.data), 1)

    ###########################################################################
    # POST
    ###########################################################################

    def test_post_member_list(self):
        """Test making POST request to create a member"""
        payload = {
            'first_name': 'Jim',
            'last_name': 'Carrey',
            'phone_number': '+12232321212',
            'client_member_id': '9999999',
            'account_id': 1,
        }
        res = self.client.post(MEMBER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        # Test that the response successfully returned the new created member
        response_member = res.data
        self.assertEqual(response_member['first_name'], payload['first_name'])
        self.assertEqual(response_member['last_name'], payload['last_name'])
        self.assertEqual(
            response_member['phone_number'], payload['phone_number']
        )
        self.assertEqual(
            response_member['client_member_id'],
            int(payload['client_member_id'])
        )
        self.assertEqual(
            int(response_member['account_id']), payload['account_id']
        )

        # Test that the member was persisted to the DB
        new_member = Member.objects.last()
        self.assertEqual(
            new_member.phone_number, response_member['phone_number']
        )
