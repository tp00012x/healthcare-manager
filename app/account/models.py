from django.db import models


class Account(models.Model):
    """Account model."""
    id = models.CharField(primary_key=True, editable=True, max_length=10)

    def __str__(self):
        return self.id
