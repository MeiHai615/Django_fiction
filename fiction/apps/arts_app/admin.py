from django.contrib import admin

# Register your models here.
import xadmin
from arts_app.models import ArtsUser, Art, Tag,Chapter
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


class ArtAdmin():
    list_display = ['art_name', 'art_info', 'art_img', 'art_tag', 'art_price', 'art_flag']
    search_fields = ['art_name', 'art_info', 'art_tag', 'art_price']
    list_filter = ['art_tag', 'art_price']
    list_per_page = 20


class TagAdmin():
    list_display = ['tag_name', 'tag_info', 'tag_create_time', 'tag_flag']
    search_fields = ['tag_name', 'tag_info']
    list_filter = ['tag_create_time', 'tag_flag']
    list_per_page = 20

class ChapterAdmin():
    list_display = ['title', 'content', 'create_time']
    search_fields = ['title', 'content']
    list_filter = ['create_time']
    list_per_page = 50

xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(ArtsUser, ArtsUserAdmin)
xadmin.site.register(Art,ArtAdmin)
xadmin.site.register(Tag,TagAdmin)
xadmin.site.register(Chapter, ChapterAdmin)