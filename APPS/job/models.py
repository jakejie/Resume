from django.db import models
from datetime import datetime


# 应聘基本信息
class JobInfo(models.Model):
    GENDER = (
        ("man", "男"),
        ("woman", "女")
    )
    DEGREE = (
        ("low", "大专以下"),
        ("dazhuan", "大专"),
        ("benke", "本科"),
        ("shuoshi", "硕士"),
        ("boshi", "博士"),
        ("other", "其他"),
    )
    MARRY = (
        ("hava", "已婚"),
        ("no", "未婚"),
        ("baby", "已育"),
        ("nobaby", "未育"),
        ("havababy", "已孕"),
        ("no_man", "离异"),
    )
    LAODONG = (
        ("in", "在职"),
        ("no", "失业"),
    )
    SHE_BAO = (
        ("neidi", "内地"),
        ("shenzhen", "深圳"),
        ("no", "无"),
    )
    ZHENGZHI = (
        ("tuan", "团员"),
        ("yu_dang", "预备党员"),
        ("dang", "党员"),
        ("qun", "群众"),
        ("qi_ta", "其他"),
    )
    JOB_FROM = (
        ("web", "招聘网站"),
        ("huiyi", "招聘会"),
        ("tuijian", "熟人推荐"),
        ("shequ", "社区推荐"),
        ("other", "其他"),
    )
    yp_center = models.CharField(verbose_name="应聘中心", max_length=100)
    yp_department = models.CharField(verbose_name="应聘部门", max_length=100)
    yp_job = models.CharField(verbose_name="应聘岗位", max_length=100)
    name = models.CharField(verbose_name="姓名", max_length=32)
    gender = models.CharField(verbose_name="性别", max_length=10, choices=GENDER)
    borthday = models.DateField(verbose_name="出生年月")
    hight = models.IntegerField(verbose_name="身高(cm)")
    weight = models.IntegerField(verbose_name="体重(kg)")
    degree = models.CharField(verbose_name="学历", max_length=10, choices=DEGREE)
    local = models.CharField(verbose_name="籍贯", max_length=100)
    marry = models.CharField(verbose_name="婚姻状况", choices=MARRY, max_length=10)
    min_zu = models.CharField(verbose_name="民族", max_length=100)
    hukou_place = models.CharField(verbose_name="户口所在地", max_length=200)
    mobile = models.CharField(verbose_name="联系电话",max_length=20)
    healthy = models.CharField(verbose_name="健康状况", max_length=32)
    laodong_connect = models.CharField(verbose_name="劳动关系现状", max_length=10, choices=LAODONG)
    she_bao = models.CharField(verbose_name="社会保险缴纳情况", max_length=10, choices=SHE_BAO)
    id_num = models.CharField(verbose_name="身份证号码",max_length=20)
    zheng_zhi = models.CharField(verbose_name="政治面貌", max_length=10, choices=ZHENGZHI)
    school_name = models.CharField(verbose_name="毕业院校", max_length=200)
    major = models.CharField(verbose_name="专业", max_length=100)
    family_place = models.CharField(verbose_name="家庭通讯地址", max_length=200)
    you_bian = models.IntegerField(verbose_name="邮编")
    dang_an_place = models.CharField(verbose_name="个人档案所在地", max_length=200)
    email = models.CharField(verbose_name="邮箱", max_length=32)
    job_from = models.CharField(verbose_name="求职来源", max_length=10, choices=JOB_FROM)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = "简历基础信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}".format(self.name)


# 工作经历
class Express(models.Model):
    username = models.ForeignKey(JobInfo, verbose_name="姓名", on_delete=models.CASCADE)
    start = models.DateField(verbose_name="工作起始日期")
    end = models.DateField(verbose_name="工作结束日期")
    dan_wei = models.CharField(verbose_name="工作单位名称", max_length=200)
    job_name = models.CharField(verbose_name="职务", max_length=100)
    xin_zi = models.CharField(verbose_name="薪资状况", max_length=20)
    reason = models.CharField(verbose_name="离职原因", max_length=100)
    people = models.CharField(verbose_name="证明人", max_length=100)
    mobile = models.CharField(verbose_name="证明人联系方式", max_length=20)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = "工作经历"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}-{}".format(self.username, self.dan_wei)


# 教育背景
class School(models.Model):
    username = models.ForeignKey(JobInfo, verbose_name="姓名", on_delete=models.CASCADE)
    start = models.DateField(verbose_name="学习起始日期")
    end = models.DateField(verbose_name="学习结束日期")
    schools = models.CharField(verbose_name="学校名称", max_length=100)
    major = models.CharField(verbose_name="专业", max_length=100)
    degree = models.CharField(verbose_name="获取学历", max_length=100)

    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = "教育背景"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}-{}".format(self.username, self.schools)


# 培训情况
class Peixun(models.Model):
    username = models.ForeignKey(JobInfo, verbose_name="姓名", on_delete=models.CASCADE)
    start = models.DateField(verbose_name="培训起始日期")
    end = models.DateField(verbose_name="培训结束日期")
    school_name = models.CharField(verbose_name="培训单位", max_length=100)
    peixin_neirong = models.CharField(verbose_name="培训内容", max_length=100)
    zhengshu = models.CharField(verbose_name="获取证书", max_length=100)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = "培训情况"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}-{}".format(self.username, self.school_name)


# 主要社会关系
class MainShehui(models.Model):
    username = models.ForeignKey(JobInfo, verbose_name="姓名", on_delete=models.CASCADE)
    connect = models.CharField(verbose_name="关系", max_length=100)
    connect_name = models.CharField(verbose_name="姓名", max_length=100)
    connect_place = models.CharField(verbose_name="家庭住址", max_length=100)
    connect_danwei = models.CharField(verbose_name="工作单位", max_length=100)
    connect_fangshi = models.CharField(verbose_name="联系方式", max_length=100)

    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = "主要社会关系"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}-{}-{}".format(self.username, self.connect, self.connect_name)
