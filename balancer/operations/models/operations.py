from django.db import models
from django.core.exceptions import ValidationError
import re

from category.models import Category
from user.models import BalancerUser


def is_valid_amount(value):
    pattern = re.compile(r'^\d+([.,]\d{2})?$')
    return bool(pattern.match(value))


def amount_validators(value):
    if not is_valid_amount(value):
        raise ValidationError('Введено неверное значение amount.')


class Operation(models.Model):
    class OperationType(models.TextChoices):
        MINUS = 'minus', 'Minus'
        PLUS = 'plus', 'Plus'

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.CharField(max_length=15, choices=OperationType.choices)
    amount = models.CharField(validators=[amount_validators], max_length=256)


class OperationsHistory(models.Model):
    user = models.ForeignKey(BalancerUser, on_delete=models.CASCADE)
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    new_balance = models.CharField(max_length=256)

    def __str__(self):
        return f'user: <{self.user}>; OPR: <{self.operation}>'