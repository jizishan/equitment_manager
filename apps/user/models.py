from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, verbose_name="联系电话")
    department = models.CharField(max_length=100, blank=True, verbose_name="部门")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name




