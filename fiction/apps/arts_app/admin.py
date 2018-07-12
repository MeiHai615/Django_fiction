from django.contrib import admin

# Register your models here.
import xadmin
from arts_app.models import ArtsUser
from xadmin import views


class BaseSetting():
    enable_themes = True
    use_bootswatch = True


class GlobalSettings():
    # 整体配置
    site_title = '小说后台管理系统'
    site_footer = 'MeiHai'
    menu_style = 'accordion'  # 菜单折叠


class ArtsUserAdmin():
    list_display = ['username', 'password', 'email', 'createtime', 'usersex']
    search_fields = ['username', 'usersex', 'email']
    list_filter = ['createtime', 'usersex']
    list_per_page = 10


xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(ArtsUser, ArtsUserAdmin)
