# Generated by Django 2.0.3 on 2018-04-16 02:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_auto_20180416_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Express',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField(verbose_name='工作起始日期')),
                ('end', models.DateField(verbose_name='工作结束日期')),
                ('dan_wei', models.CharField(max_length=200, verbose_name='工作单位名称')),
                ('job_name', models.CharField(max_length=100, verbose_name='职务')),
                ('xin_zi', models.CharField(max_length=20, verbose_name='薪资状况')),
                ('reason', models.CharField(max_length=100, verbose_name='离职原因')),
                ('people', models.CharField(max_length=100, verbose_name='证明人')),
                ('mobile', models.CharField(max_length=20, verbose_name='证明人联系方式')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '工作经历',
                'verbose_name_plural': '工作经历',
            },
        ),
        migrations.CreateModel(
            name='MainShehui',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connect', models.CharField(max_length=100, verbose_name='关系')),
                ('connect_name', models.CharField(max_length=100, verbose_name='姓名')),
                ('connect_place', models.CharField(max_length=100, verbose_name='家庭住址')),
                ('connect_danwei', models.CharField(max_length=100, verbose_name='工作单位')),
                ('connect_fangshi', models.CharField(max_length=100, verbose_name='联系方式')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '主要社会关系',
                'verbose_name_plural': '主要社会关系',
            },
        ),
        migrations.CreateModel(
            name='Peixun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField(verbose_name='培训起始日期')),
                ('end', models.DateField(verbose_name='培训结束日期')),
                ('school_name', models.CharField(max_length=100, verbose_name='培训单位')),
                ('peixin_neirong', models.CharField(max_length=100, verbose_name='培训内容')),
                ('zhengshu', models.CharField(max_length=100, verbose_name='获取证书')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '培训情况',
                'verbose_name_plural': '培训情况',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField(verbose_name='学习起始日期')),
                ('end', models.DateField(verbose_name='学习结束日期')),
                ('schools', models.CharField(max_length=100, verbose_name='学校名称')),
                ('major', models.CharField(max_length=100, verbose_name='专业')),
                ('degree', models.CharField(max_length=100, verbose_name='获取学历')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '教育背景',
                'verbose_name_plural': '教育背景',
            },
        ),
        migrations.RenameField(
            model_name='jobinfo',
            old_name='school',
            new_name='school_name',
        ),
        migrations.AddField(
            model_name='school',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.JobInfo', verbose_name='姓名'),
        ),
        migrations.AddField(
            model_name='peixun',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.JobInfo', verbose_name='姓名'),
        ),
        migrations.AddField(
            model_name='mainshehui',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.JobInfo', verbose_name='姓名'),
        ),
        migrations.AddField(
            model_name='express',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.JobInfo', verbose_name='姓名'),
        ),
    ]