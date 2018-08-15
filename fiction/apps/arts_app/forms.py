# -*- coding: utf-8 -*-
__author__ = 'MeiHai'
__date__ = '2018/7/11 19:06'
from django import forms
from django.forms import widgets
from arts_app.models import ArtsUser
from django.core.exceptions import ValidationError

from captcha.fields import CaptchaField
'''
注册表单
'''


class ArtsuserRegForm(forms.Form):
    username = forms.CharField(
        label='用户名',
        required=True,
        max_length=20,
        min_length=6,

        widget=widgets.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '请输入用户名,长度为6~20',

            }
        ),
        error_messages={
            'required': '对不起,用户名不能为空!',
            "min_length": '用户名长度不能小于6位',
            "max_length": "用户名长度不能大于20",
        }
    )
    password = forms.CharField(

        label='密码',
        required=True,
        min_length=6,
        max_length=20,
        widget=widgets.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "请输入密码, 长度为6~20",
            }
        ),
        error_messages={

            "required": "对不起，密码不能为空！",
            "min_length": "不行，长度小于6",
            "max_length": "sorry, 长度太长，大于20",
        }

    )
    confirm_password = forms.CharField(
        label='确认密码',
        required=True,
        widget=widgets.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '请确认密码'
            }
        ),
        error_messages={
            'required': '确认密码不能为空',

        }
    )

    email = forms.EmailField(
        label="邮箱",
        required=True,
        widget=widgets.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "请输入邮箱",
            }),
        error_messages={
            "required": "对不起，邮箱不能为空！",
        }
    )

    def clean_username(self):

        username = self.cleaned_data.get('username', '')
        users = ArtsUser.objects.filter(username=username)
        if users:
            raise ValidationError('用户名已存在！！！')
        return username

    def clean_password(self):
        import re
        password = self.cleaned_data.get('password', '')

        res = re.compile('(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z_]')
        ps = res.findall(password)
        if not ps:
            raise ValidationError('密码必须包含字母跟数字')
        return password

    def clean_confirm_password(self):
        passwd = self.cleaned_data.get('confirm_password', '')
        password = self.clean_password()
        if password != passwd:
            raise ValidationError('两次输入的密码不一致！！！')
        return password

    def clean_email(self):
        # 对email字段进行校验
        email = self.cleaned_data.get("email", "")
        users = ArtsUser.objects.filter(email=email).count()
        if users:
            raise ValidationError("邮箱已经存在！")
        return email


'''
登录表单
'''


class LoginForm(forms.Form):
    username = forms.CharField(
        label="用户名",
        required=True,
        min_length=6,
        max_length=20,
        widget=widgets.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "请输入用户名，长度为6 ~ 20",
            }),
        error_messages={
            "required": "对不起，输入的用户名不能为空",
            "min_length": "不行, 长度小于6",
            "max_length": "sorry, 长度大于20",
        }
    )
    password = forms.CharField(
        label="密码",
        required=True,
        min_length=6,
        max_length=20,
        widget=widgets.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "请输入密码, 长度为6~20",
            }),
        error_messages={
            "required": "密码不能为空",
            "min_length": "密码长度不能小于6",
            "max_length": "密码长度不能大于20",
        }
    )
    captcha = CaptchaField(label='验证码', error_messages={'invalid': '验证码输入有误'})


