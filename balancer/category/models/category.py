from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Название категории', max_length=50, unique=True)


class ChildCategory(models.Model):
    name = models.CharField(verbose_name='Название категории', max_length=50, unique=True)
    parent_category = models.ForeignKey(Category, on_delete=models.CASCADE)
