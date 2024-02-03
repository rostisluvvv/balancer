from django.db import models
from django.utils import timezone


class BalancerUser(models.Model):
    tg_token = models.CharField(max_length=256, unique=True, null=False, blank=False)
    date_joined = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'user_id: {self.pk}'
