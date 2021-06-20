# Generated by Django 2.2.2 on 2021-06-20 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210607_2032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='study',
            name='degree',
        ),
        migrations.AlterField(
            model_name='course',
            name='course_type',
            field=models.IntegerField(choices=[(1, 'درس اصلی'), (2, 'درس تخصصی'), (3, 'درس عمومی'), (4, 'درس اختیاری'), (5, 'درس پایه')], verbose_name='نوع درس'),
        ),
    ]
