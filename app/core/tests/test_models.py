from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_superuser_with_email_successful(self):
        """Test creating a new superuser with an email is successful."""
        email = 'anthony@gmail.com'
        password = 'password'
        superuser = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )

        self.assertEqual(superuser.email, email)
        self.assertTrue(superuser.check_password(password))

    def test_new_superuser_email_normalized(self):
        """Testing create superuser and normalizing the email address."""
        email = 'anthony@GMAIL.com'
        user = get_user_model().objects.create_superuser(email, 'password')

        self.assertEqual(user.email, email.lower())

    def test_new_superuser_invalid_email(self):
        """Test create superuser with invalid email."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_superuser(None, 'password')

    def test_create_new_superuser(self):
        """Test create new superuser"""
        superuser = get_user_model().objects.create_superuser(
            'anthony@gmail.com',
            'password'
        )

        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)
