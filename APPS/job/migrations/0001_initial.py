# Generated by Django 2.0.3 on 2018-04-16 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yp_center', models.CharField(max_length=100, verbose_name='应聘中心')),
                ('yp_department', models.CharField(max_length=100, verbose_name='应聘部门')),
                ('yp_job', models.CharField(max_length=100, verbose_name='应聘岗位')),
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
                ('gender', models.CharField(choices=[('man', '男'), ('woman', '女')], max_length=10, verbose_name='性别')),
                ('borthday', models.DateField(verbose_name='出生年月')),
                ('hight', models.IntegerField(verbose_name='身高(cm)')),
                ('weight', models.IntegerField(verbose_name='体重(kg)')),
                ('degree', models.CharField(choices=[('low', '大专以下'), ('dazhuan', '大专'), ('benke', '本科'), ('shuoshi', '硕士'), ('boshi', '博士'), ('other', '其他')], max_length=10, verbose_name='学历')),
                ('local', models.CharField(max_length=100, verbose_name='籍贯')),
                ('marry', models.CharField(choices=[('hava', '已婚'), ('no', '未婚'), ('baby', '已育'), ('nobaby', '未育'), ('havababy', '已孕'), ('no_man', '离异')], max_length=10, verbose_name='婚姻状况')),
                ('min_zu', models.CharField(max_length=100, verbose_name='民族')),
                ('hukou_place', models.CharField(max_length=200, verbose_name='户口所在地')),
                ('mobile', models.IntegerField(verbose_name='联系电话')),
                ('healthy', models.CharField(max_length=32, verbose_name='健康状况')),
                ('laodong_connect', models.CharField(choices=[('in', '在职'), ('no', '失业')], max_length=10, verbose_name='劳动关系现状')),
                ('she_bao', models.CharField(choices=[('neidi', '内地'), ('shenzhen', '深圳'), ('no', '无')], max_length=10, verbose_name='社会保险缴纳情况')),
                ('id_num', models.IntegerField(verbose_name='身份证号码')),
                ('zheng_zhi', models.CharField(choices=[('tuan', '团员'), ('yu_dang', '预备党员'), ('dang', '党员'), ('qun', '群众'), ('qi_ta', '其他')], max_length=10, verbose_name='政治面貌')),
                ('school', models.CharField(max_length=200, verbose_name='毕业院校')),
                ('major', models.CharField(max_length=100, verbose_name='专业')),
                ('family_place', models.CharField(max_length=200, verbose_name='家庭通讯地址')),
                ('you_bian', models.IntegerField(verbose_name='邮编')),
                ('dang_an_place', models.CharField(max_length=200, verbose_name='个人档案所在地')),
                ('email', models.CharField(max_length=32, verbose_name='邮箱')),
                ('job_from', models.CharField(choices=[('web', '招聘网站'), ('huiyi', '招聘会'), ('tuijian', '熟人推荐'), ('shequ', '社区推荐'), ('other', '其他')], max_length=10, verbose_name='求职来源')),
            ],
        ),
    ]