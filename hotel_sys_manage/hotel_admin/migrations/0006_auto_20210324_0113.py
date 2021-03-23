# Generated by Django 2.2 on 2021-03-23 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_admin', '0005_auto_20210323_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel_nightlyrate_info',
            name='cose',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='价格'),
        ),
        migrations.AlterField(
            model_name='room_image_info',
            name='imageLogo',
            field=models.IntegerField(choices=[(1, '无水印logo'), (-1, '未知'), (0, '有水印logo')], default=-1, verbose_name='是否带水印'),
        ),
        migrations.AlterField(
            model_name='room_image_info',
            name='imageSize',
            field=models.IntegerField(choices=[(3, '640 * 960'), (0, '未分类'), (2, '550 * 412'), (1, '350 * 350')], default=0, verbose_name='图片规格'),
        ),
    ]