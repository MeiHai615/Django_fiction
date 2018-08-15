from django.db import models

# Create your models here.
from arts_app.models import ArtsUser

class OAuth_ex(models.Model):
    user = models.CharField(max_length=12, null=True, verbose_name='QQ用户名')
    qq_openid = models.CharField(max_length=64, null=True)

    def __str__(self):
        return '%s' %(self.user)

    class Meta:
        verbose_name = 'qq用户'
        verbose_name_plural = verbose_name
        db_table = 'oauth_qq'
