from account.models import Account
from core.models import BaseUser
from django.contrib.auth.models import BaseUserManager
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class MemberManager(BaseUserManager):
    def create_dummy_member(self,
                            phone_number='+15555555555',
                            client_member_id=1111111,
                            ):
        """Util function to expedite creating a dummy member."""
        account = Account.objects.create(id=1)
        return self.create(
            first_name='Dwight',
            last_name='Schrute',
            account_id=account,
            phone_number=phone_number,
            client_member_id=client_member_id,
        )


class Member(BaseUser):
    """Member model."""
    phone_number = PhoneNumberField(unique=True)
    client_member_id = models.PositiveIntegerField(unique=True)
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)

    objects = MemberManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
