# Generated by Django 2.2 on 2021-03-23 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_admin', '0006_auto_20210324_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room_image_info',
            name='imageLogo',
            field=models.IntegerField(choices=[(-1, '未知'), (0, '有水印logo'), (1, '无水印logo')], default=-1, verbose_name='是否带水印'),
        ),
        migrations.AlterField(
            model_name='room_image_info',
            name='imageSize',
            field=models.IntegerField(choices=[(3, '640 * 960'), (2, '550 * 412'), (0, '未分类'), (1, '350 * 350')], default=0, verbose_name='图片规格'),
        ),
    ]