from django.db import models
from apps.user.models import User

class Equipment(models.Model):
    STATUS_CHOICES = (
        ('in_stock', '在库'),
        ('in_use', '使用中'),
        ('maintenance', '维护中'),
    )

    name = models.CharField(max_length=100, verbose_name="设备名称")
    model = models.CharField(max_length=100, verbose_name="型号")
    serial_number = models.CharField(max_length=100, unique=True, verbose_name="序列号")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_stock')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="负责人")
    purchase_date = models.DateField(verbose_name="购置日期")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.model})"