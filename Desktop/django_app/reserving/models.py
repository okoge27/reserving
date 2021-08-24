from accounts.models import CustomUser
from django.db import models
from django.db.models.fields import TextField
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.conf import settings
from django.utils import timezone

choice = (
    ('車検', '車検'),
    ('修理', '修理'),
    ('その他', 'その他')
)

class Reserve(models.Model):
    """customuser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="ユーザー", related_name='customuser')"""
    customer_name = models.CharField('お名前', max_length=20)
    reserve_date = models.DateTimeField('予約日時', default=timezone.now)
    contents = models.CharField('予約内容', choices=choice, max_length=5, blank=True, default=0)

    def __str__(self):
        return "{}様 予約内容:{} 日時:{}".format(self.customer_name, self.contents, self.reserve_date)


class Log(models.Model):
    text = models.TextField('備考')
    reserve = models.ForeignKey(Reserve, on_delete=models.CASCADE, verbose_name="予約", related_name='log')
    def __str__(self):
        return self.text
