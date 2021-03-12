# Generated by Django 2.2 on 2021-03-12 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_admin', '0002_auto_20210312_1018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room_info',
            old_name='basisroomid',
            new_name='basisroomId',
        ),
        migrations.RemoveField(
            model_name='room_info',
            name='id',
        ),
        migrations.AddField(
            model_name='room_info',
            name='bedName',
            field=models.CharField(default='', max_length=100, verbose_name='名称'),
        ),
        migrations.AddField(
            model_name='room_info',
            name='bedType',
            field=models.CharField(default='', max_length=50, verbose_name='类型'),
        ),
        migrations.AlterField(
            model_name='price_model_info',
            name='level',
            field=models.IntegerField(choices=[(1, '节假日'), (2, '自定义'), (0, '默认'), (9, '最高级')], default=0, verbose_name='优先级'),
        ),
        migrations.AlterField(
            model_name='room_image_info',
            name='imageLogo',
            field=models.IntegerField(choices=[(1, '无水印logo'), (-1, '未知'), (0, '有水印logo')], default=-1, verbose_name='是否带水印'),
        ),
        migrations.AlterField(
            model_name='room_image_info',
            name='imageSize',
            field=models.IntegerField(choices=[(3, '640 * 960'), (1, '350 * 350'), (0, '未分类'), (2, '550 * 412')], default=0, verbose_name='图片规格'),
        ),
        migrations.AlterField(
            model_name='room_info',
            name='roomTypeId',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='房型编号'),
        ),
    ]
