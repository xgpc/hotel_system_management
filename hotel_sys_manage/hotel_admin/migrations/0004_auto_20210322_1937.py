# Generated by Django 2.2 on 2021-03-22 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_admin', '0003_auto_20210314_0125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price_model_info',
            name='sys_create_user',
        ),
        migrations.AlterModelOptions(
            name='hotel_nightlyrate_info',
            options={'managed': True, 'verbose_name': '间夜价格数据', 'verbose_name_plural': '间夜价格数据'},
        ),
        migrations.AlterField(
            model_name='hotel_bookingrule_info',
            name='bookingRuleId',
            field=models.CharField(max_length=500, verbose_name='预订条款编号'),
        ),
        migrations.AlterField(
            model_name='hotel_info',
            name='introduceCn',
            field=models.TextField(default='无', verbose_name='酒店中文介绍'),
        ),
        migrations.AlterField(
            model_name='hotel_info',
            name='introduceEn',
            field=models.TextField(default='无', verbose_name='酒店英文介绍'),
        ),
        migrations.AlterField(
            model_name='room_image_info',
            name='imageLogo',
            field=models.IntegerField(choices=[(-1, '未知'), (0, '有水印logo'), (1, '无水印logo')], default=-1, verbose_name='是否带水印'),
        ),
        migrations.AlterField(
            model_name='room_image_info',
            name='imageSize',
            field=models.IntegerField(choices=[(3, '640 * 960'), (0, '未分类'), (2, '550 * 412'), (1, '350 * 350')], default=0, verbose_name='图片规格'),
        ),
        migrations.DeleteModel(
            name='Order_info',
        ),
        migrations.DeleteModel(
            name='Price_model_info',
        ),
    ]