from django.db import models
from django.utils import timezone
# Create your models here.
from fiction.settings import SEX_CHOICES, FLAGS_CHOICES, DINNER_CHOICES, PAY_CHOICES, DB_FIELD_VALID_CHOICES
from django.conf import settings

'''
用户信息
'''


class ArtsUser(models.Model):
    username = models.CharField(max_length=50, verbose_name='用户名')
    password = models.CharField(max_length=100, verbose_name='密码')
    email = models.EmailField(verbose_name='邮箱')
    createtime = models.DateTimeField(default=timezone.now, db_index=True,
                                      verbose_name='添加时间')
    flag = models.IntegerField(default=0, verbose_name='控制字段', choices=FLAGS_CHOICES)
    usersex = models.CharField(max_length=10, default=0, verbose_name='性别', choices=SEX_CHOICES)
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '会员信息'
        verbose_name_plural = verbose_name
        db_table = 'arts_user'
        ordering = ['-createtime']


class Ip(models.Model):
    ip = models.CharField(max_length=20, verbose_name='ip地址')

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name = 'ip地址'
        verbose_name_plural = verbose_name
        db_table = 'ip_addr'


'''
小说类别
'''


class Tag(models.Model):
    tag_name = models.CharField(max_length=32, verbose_name='类别')
    tag_info = models.CharField(max_length=64, verbose_name='类别描述')
    tag_create_time = models.DateTimeField(default=timezone.now, db_index=True, verbose_name='创建时间')
    tag_flag = models.IntegerField(default=0, verbose_name='控制字段', choices=DB_FIELD_VALID_CHOICES)

    def __str__(self):
        return self.tag_name

    class Meta:
        db_table = 'tag'
        verbose_name = '小说类别'
        verbose_name_plural = verbose_name
        ordering = ['-tag_create_time']


'''
小说信息
'''


class Art(models.Model):
    art_name = models.CharField(max_length=32, verbose_name='书名')
    art_info = models.CharField(max_length=255, verbose_name='简单描述')
    art_img = models.ImageField(max_length=150, verbose_name='封面', upload_to='media/arts_ups/%Y/%m')
    art_create_time = models.DateTimeField(default=timezone.now, db_index=True, verbose_name='更新时间')
    art_tag = models.ForeignKey(Tag, verbose_name='关联类别标签')
    art_price = models.IntegerField(default=0, verbose_name='单价')
    art_flag = models.IntegerField(default=0, verbose_name='小说控制字段', choices=DB_FIELD_VALID_CHOICES)

    def __str__(self):
        return self.art_name

    class Meta:
        db_table = 'art'
        verbose_name = '小说'
        verbose_name_plural = verbose_name
        ordering = ['-art_create_time']


'''
章节信息
'''

class Chapter(models.Model):
    art = models.ForeignKey(Art, verbose_name="小说")
    title = models.CharField(max_length=100, verbose_name="章节标题")
    content = models.TextField(verbose_name="小说章节内容")
    create_time = models.DateTimeField(default=timezone.now, db_index=True,
                                       verbose_name="添加时间")

    class Meta:
        db_table = "art_chapter"
        verbose_name = "小说章节"
        verbose_name_plural = verbose_name
