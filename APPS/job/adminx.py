# -*- coding:utf-8 -*-
__author__ = "jake"
__email__ = "jakejie@163.com"
"""
Project:jobguanli
FileName = PyCharm
Version:1.0
CreateDay:2018/4/16 9:55
"""
import xadmin
from .models import JobInfo, Express, School, Peixun, MainShehui


class JonInfoAdmin(object):
    # 配置后台我们需要显示的列
    list_display = ['yp_center', 'yp_department', 'yp_job', 'name', 'school_name', 'major']
    # 配置搜索字段,不做时间搜索
    search_fields = ['yp_center', 'yp_department', 'yp_job', 'name', 'school_name', 'major']
    # 配置筛选字段
    list_filter = ['yp_center', 'yp_department', 'yp_job', 'name', 'school_name', 'major']


class ExpressAdmin(object):
    # 配置后台我们需要显示的列
    list_display = ['username', 'start', 'end', 'dan_wei', 'job_name', 'xin_zi', 'add_time']
    # 配置搜索字段,不做时间搜索
    search_fields = ['username', 'start', 'end', 'dan_wei', 'job_name', 'xin_zi', 'add_time']
    # 配置筛选字段
    list_filter = ['username', 'start', 'end', 'dan_wei', 'job_name', 'xin_zi', 'add_time']


class SchoolAdmin(object):
    # 配置后台我们需要显示的列
    list_display = ['username', 'start', 'end', 'schools', 'major', 'degree', 'add_time']
    # 配置搜索字段,不做时间搜索
    search_fields = ['username', 'start', 'end', 'schools', 'major', 'degree', 'add_time']
    # 配置筛选字段
    list_filter = ['username', 'start', 'end', 'schools', 'major', 'degree', 'add_time']


class PeixunAdmin(object):
    # 配置后台我们需要显示的列
    list_display = ['username', 'start', 'end', 'school_name', 'peixin_neirong', 'zhengshu', 'add_time']
    # 配置搜索字段,不做时间搜索
    search_fields = ['username', 'start', 'end', 'school_name', 'peixin_neirong', 'zhengshu', 'add_time']
    # 配置筛选字段
    list_filter = ['username', 'start', 'end', 'school_name', 'peixin_neirong', 'zhengshu', 'add_time']


class MainShehuiAdmin(object):
    # 配置后台我们需要显示的列
    list_display = ['username', 'connect', 'connect_name', 'connect_place', 'connect_danwei', 'connect_fangshi', 'add_time']
    # 配置搜索字段,不做时间搜索
    search_fields = ['username', 'connect', 'connect_name', 'connect_place', 'connect_danwei', 'connect_fangshi',
                     'add_time']
    # 配置筛选字段
    list_filter = ['username', 'connect', 'connect_name', 'connect_place', 'connect_danwei', 'connect_fangshi', 'add_time']


xadmin.site.register(JobInfo, JonInfoAdmin)
xadmin.site.register(Express, ExpressAdmin)
xadmin.site.register(School, SchoolAdmin)
xadmin.site.register(Peixun, PeixunAdmin)
xadmin.site.register(MainShehui, MainShehuiAdmin)

from xadmin import views


# 创建X admin的全局管理器并与view绑定。
class BaseSetting(object):
    # 开启主题功能
    enable_themes = True
    use_bootswatch = True


# xadmin全局配置
class GlobalSettings(object):
    site_title = "方特简历管理系统"
    site_footer = "方特简历管理系统"


# 将全局配置管理与view绑定注册
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

if __name__ == "__main__":
    pass
