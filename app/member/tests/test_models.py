from django.db.utils import IntegrityError
from django.test import TestCase
from member.models import Member


class ModelTests(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.phone_number = '+15551112222'
        self.client_member_id = 1111111
        self.member = Member.objects.create(
            first_name='Dwight',
            last_name='Schrute',
            phone_number=self.phone_number,
            client_member_id=self.client_member_id,
            account_id=12,
        )

    def test_create_successful_member(self):
        """Test creating a new member successfully"""
        db_member = Member.objects.last()
        self.assertEqual(db_member, self.member)

    def test_create_member_with_existing_phone_number(self):
        """
        Test creating a new member that matches another member's phone number.
        """
        with self.assertRaises(IntegrityError):
            Member.objects.create(
                first_name='Jim',
                last_name='Halpert',
                phone_number=self.phone_number,
                client_member_id=2222222,
                account_id=12,
            )

    def test_create_member_with_existing_client_member_id(self):
        """
        Test creating a new member that matches another member's client memeber
        id.
        """
        with self.assertRaises(IntegrityError):
            Member.objects.create(
                first_name='Jim',
                last_name='Halpert',
                phone_number='+11234567890',
                client_member_id=self.client_member_id,
                account_id=12,
            )
