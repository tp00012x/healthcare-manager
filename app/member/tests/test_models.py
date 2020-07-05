from django.db.utils import IntegrityError
from django.test import TestCase
from member.models import Member


class ModelTests(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.member = Member.objects.create_dummy_member()

    def test_create_successful_member(self):
        """Test creating a new member successfully"""
        db_member = Member.objects.last()
        self.assertEqual(db_member, self.member)

    def test_create_member_with_existing_phone_number(self):
        """
        Test creating a new member that matches another member's phone number.
        """
        with self.assertRaises(IntegrityError):
            Member.objects.create_dummy_member(client_member_id=2222222)

    def test_create_member_with_existing_client_member_id(self):
        """
        Test creating a new member that matches another member's client memeber
        id.
        """
        with self.assertRaises(IntegrityError):
            Member.objects.create_dummy_member(phone_number='+11234567890')
