from account.models import Account
from core.models import BaseUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Member(BaseUser):
    """Member model."""
    phone_number = PhoneNumberField(unique=True)
    client_member_id = models.PositiveIntegerField(unique=True)
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
