from core.models import BaseUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Member(BaseUser):
    """Member model."""
    phone_number = PhoneNumberField(unique=True)
    client_member_id = models.PositiveIntegerField(unique=True)
    account_id = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
