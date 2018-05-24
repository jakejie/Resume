# -*- coding:utf-8 -*-
__author__ = "jake"
__email__ = "jakejie@163.com"
"""
Project:jobguanli
FileName = PyCharm
Version:1.0
CreateDay:2018/4/16 11:27
"""
# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy import Column, String, create_engine, Integer, Text, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, query
# from xlwt import Workbook
import xlwt

book = xlwt.Workbook()
# 设置字体
font = xlwt.Font()
font.name = 'SimSun'  # 指定“宋体”
font.bold = True
font.underline = True
font.italic = True
style = xlwt.XFStyle()
style.font = font
style.font.height = 430  # 设置字体大小


# 数据库连接信息
db_host = '*'
db_user = 'excel'
db_pawd = 'excelpassword'
db_name = 'fangte'
db_port = 3306
# 创建对象的基类:
Base = declarative_base()
engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'
                       .format(db_user, db_pawd, db_host, db_port, db_name), max_overflow=500)

Base.metadata.reflect(engine)
db_session = scoped_session(sessionmaker(bind=engine))


# 操作已经存在的数据表
class JobInfo(Base):
    __table__ = Base.metadata.tables['job_jobinfo']


class Express(Base):
    __table__ = Base.metadata.tables['job_express']


class School(Base):
    __table__ = Base.metadata.tables['job_school']


class Peixun(Base):
    __table__ = Base.metadata.tables['job_peixun']


class MainShehui(Base):
    __table__ = Base.metadata.tables['job_mainshehui']


class JobGuanli(object):
    def __init__(self):
        # 初始化数据库连接,:
        engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'
                               .format(db_user, db_pawd, db_host, db_port, db_name), max_overflow=500)
        # 创建DBSession类型:
        # DBSession = sessionmaker(bind=engine)
        # self.session = DBSession()
        Base.metadata.reflect(engine)
        self.session = scoped_session(sessionmaker(bind=engine))

    def input_user(self):
        print("输入要导出的名字".center(10, '*'))
        username = input("姓名：")
        # username = "朱杰"
        return username

    # 根据用户名 提取所有相关信息
    def get_info(self, username):
        base_info = self.session.query(JobInfo).filter_by(name=username).first()
        express = self.session.query(Express).filter_by(username_id=base_info.id).all()
        school = self.session.query(School).filter_by(username_id=base_info.id).all()
        peixun = self.session.query(Peixun).filter_by(username_id=base_info.id).all()
        shehui = self.session.query(MainShehui).filter_by(username_id=base_info.id).all()
        return base_info, express, school, peixun, shehui

    # 写入成excel文件
    def create_excel(self, username, base_info, express, school, peixun, shehui):
        sheet1 = book.add_sheet("{}".format(username))
        first_col = sheet1.col(0)
        first_col.width = 256 * 20

        # 基础信息
        self.write_basic(sheet1, base_info)
        # 工作经历
        sheet1.write_merge(16, 16, 0, 6, "工作经历（按由后至前的方式登记）")
        self.write_express(sheet1, express)
        # 教育背景
        sheet1.write_merge(22, 22, 0, 6, "教育背景（按学历由高至低的方式登记，不记小学）")
        self.write_school(sheet1, school)
        # 接受培训情况
        sheet1.write_merge(27, 27, 0, 6, "接受培训情况")
        self.write_peixin(sheet1, peixun)
        # 主要社会关系
        sheet1.write_merge(31, 31, 0, 6, "主要社会关系(直系亲属)")
        self.write_shehui(sheet1, shehui)

    # 基础信息
    def write_basic(self, sheet1, base_info):
        # 第六行
        sheet1.write(5, 0, "应聘中心")
        sheet1.write(5, 1, base_info.yp_center)
        sheet1.write(5, 2, "应聘部门")
        sheet1.write(5, 3, base_info.yp_department)
        sheet1.write(5, 4, "应聘岗位")
        sheet1.write(5, 5, base_info.yp_job)
        # 第七行
        sheet1.write(6, 0, "姓名")
        sheet1.write(6, 1, base_info.name)
        sheet1.write(6, 2, "性别")
        if base_info.gender == "man":
            genders = "男"
        else:
            genders = "女"
        sheet1.write(6, 3, genders)
        sheet1.write(6, 4, "出生年月")
        sheet1.write(6, 5, str(base_info.borthday))
        # 第八行
        sheet1.write(7, 0, "身高(cm)")
        sheet1.write(7, 1, base_info.hight)
        sheet1.write(7, 2, "体重(kg)")
        sheet1.write(7, 3, base_info.weight)
        sheet1.write(7, 4, "学历")
        if base_info.degree == "low":
            degrees = "大专以下"
        elif base_info.degree == "dazhuan":
            degrees = "大专"
        elif base_info.degree == "benke":
            degrees = "本科"
        elif base_info.degree == "shuoshi":
            degrees = "硕士"
        elif base_info.degree == "boshi":
            degrees = "博士"
        else:
            degrees = "其他"
        sheet1.write(7, 5, degrees)
        # 第九行
        sheet1.write(8, 0, "籍贯")
        sheet1.write(8, 1, base_info.local)
        sheet1.write(8, 2, "婚姻状况")
        if base_info.marry == "hava":
            marrys = "已婚"
        elif base_info.marry == "no":
            marrys = "未婚"
        elif base_info.marry == "baby":
            marrys = "已育"
        elif base_info.marry == "nobaby":
            marrys = "未育"
        elif base_info.marry == "havababy":
            marrys = "已孕"
        else:
            marrys = "离异"
        sheet1.write(8, 3, marrys)
        # 第十行
        sheet1.write(9, 0, "民族")
        sheet1.write(9, 1, base_info.min_zu)
        sheet1.write(9, 2, "户口所在地")
        sheet1.write(9, 3, base_info.hukou_place)
        sheet1.write(9, 4, "联系电话")
        sheet1.write(9, 5, base_info.mobile)
        # 第十一行
        sheet1.write(10, 0, "健康状况")
        sheet1.write(10, 1, base_info.healthy)
        sheet1.write(10, 2, "劳动关系现状")
        if base_info.laodong_connect == "in":
            laodong_connects = "在职"
        else:
            laodong_connects = "失业"
        sheet1.write(10, 3, laodong_connects)
        sheet1.write(10, 4, "社会保险缴纳情况")
        if base_info.she_bao == "neidi":
            she_baos = "内地"
        elif base_info.she_bao == "shenzhen":
            she_baos = "深圳"
        else:
            she_baos = "无"
        sheet1.write(10, 5, she_baos)
        # 第十二行
        sheet1.write_merge(11, 11, 0, 1, "身份证号码")
        sheet1.write_merge(11, 11, 2, 3, base_info.id_num)
        sheet1.write(11, 4, "政治面貌")
        if base_info.zheng_zhi == "tuan":
            zheng_zhis = "团员"
        elif base_info.zheng_zhi == "yu_dang":
            zheng_zhis = "预备党员"
        elif base_info.zheng_zhi == "dang":
            zheng_zhis = "党员"
        elif base_info.zheng_zhi == "qun":
            zheng_zhis = "群众"
        else:
            zheng_zhis = "其他"
        sheet1.write_merge(11, 11, 5, 6, zheng_zhis)
        # 第十三行
        sheet1.write_merge(12, 12, 0, 1, "毕业院校")
        sheet1.write_merge(12, 12, 2, 3, base_info.school_name)
        sheet1.write(12, 4, "专业")
        sheet1.write_merge(12, 12, 5, 6, base_info.major)
        # 第十四行
        sheet1.write_merge(13, 13, 0, 1, "家庭通讯地址")
        sheet1.write_merge(13, 13, 2, 3, base_info.family_place)
        sheet1.write(13, 4, "邮编")
        sheet1.write_merge(13, 13, 5, 6, base_info.you_bian)
        # 第十五行
        sheet1.write_merge(14, 14, 0, 1, "个人档案所在地")
        sheet1.write_merge(14, 14, 2, 3, base_info.dang_an_place)
        sheet1.write(14, 4, "邮箱")
        sheet1.write_merge(14, 14, 5, 6, base_info.email)
        # 第十六行
        sheet1.write_merge(15, 15, 0, 1, "求职来源")
        if base_info.job_from == "web":
            job_froms = "招聘网站"
        elif base_info.job_from == "huiyi":
            job_froms = "招聘会"
        elif base_info.job_from == "tuijian":
            job_froms = "熟人推荐"
        elif base_info.job_from == "shequ":
            job_froms = "社区推荐"
        else:
            job_froms = "其他"
        sheet1.write_merge(15, 15, 2, 5, job_froms)

    # 工作经历
    def write_express(self, sheet1, express):
        # 第18行
        sheet1.write(17, 0, "起止年月")
        sheet1.write(17, 1, "工作单位名称")
        sheet1.write(17, 2, "职务")
        sheet1.write(17, 3, "薪资状况")
        sheet1.write(17, 4, "离职原因")
        sheet1.write(17, 5, "证明人")
        sheet1.write(17, 6, "联系方式")
        # 第19行
        for index, work in enumerate(express):
            if index < 3:
                sheet1.write(18 + index, 0, str(work.start) + "-" + str(work.end))
                sheet1.write(18 + index, 1, work.dan_wei)
                sheet1.write(18 + index, 2, work.job_name)
                sheet1.write(18 + index, 3, work.xin_zi)
                sheet1.write(18 + index, 4, work.reason)
                sheet1.write(18 + index, 5, work.people)
                sheet1.write(18 + index, 6, work.mobile)

    # 教育背景
    def write_school(self, sheet1, school):
        # 第24行
        sheet1.write_merge(23, 23, 0, 1, "学习起止年月")
        sheet1.write_merge(23, 23, 2, 4, "学校名称")
        sheet1.write(23, 5, "专业")
        sheet1.write(23, 6, "获取学历")
        for index, schools in enumerate(school):
            if index < 3:
                sheet1.write_merge(24 + index, 24 + index, 0, 1, str(schools.start) + "-" + str(schools.end))
                sheet1.write_merge(24 + index, 24 + index, 2, 4, schools.schools)
                sheet1.write(24 + index, 5, schools.major)
                sheet1.write(24 + index, 6, schools.degree)

    # 接受培训情况
    def write_peixin(self, sheet1, peixun):
        # 第29行
        sheet1.write_merge(28, 28, 0, 1, "培训起止年月")
        sheet1.write_merge(28, 28, 2, 4, "培训单位")
        sheet1.write(28, 5, "培训内容")
        sheet1.write(28, 6, "获取证书")
        for index, pei in enumerate(peixun):
            if index < 3:
                sheet1.write_merge(29 + index, 29 + index, 0, 1, str(pei.start) + "-" + str(pei.end))
                sheet1.write_merge(29 + index, 29 + index, 2, 4, pei.school_name)
                sheet1.write(29 + index, 5, pei.peixin_neirong)
                sheet1.write(29 + index, 6, pei.zhengshu)

    # 主要社会关系(直系亲属)
    def write_shehui(self, sheet1, shehui):
        # 第29行
        sheet1.write(32, 0, "关系")
        sheet1.write(32, 1, "姓名")
        sheet1.write_merge(32, 32, 2, 4, "家庭住址")
        sheet1.write(32, 5, "工作单位")
        sheet1.write(32, 6, "联系方式")
        for index, she in enumerate(shehui):
            if index < 3:
                sheet1.write(33 + index, 0, she.connect)
                sheet1.write(33 + index, 1, she.connect_name)
                sheet1.write_merge(33 + index, 33 + index, 2, 4, she.connect_place)
                sheet1.write(33 + index, 5, she.connect_danwei)
                sheet1.write(33 + index, 6, she.connect_fangshi)


if __name__ == "__main__":
    job = JobGuanli()
    username = job.input_user()
    base_info, express, school, peixun, shehui = job.get_info(username)
    job.create_excel(username, base_info, express, school, peixun, shehui)
    book.save("{}.xls".format(username))
