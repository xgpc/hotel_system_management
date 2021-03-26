# Generated by Django 2.2 on 2021-03-25 15:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotel_admin', '0008_auto_20210324_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city_info',
            name='is_effective',
            field=models.IntegerField(choices=[(1, '启用'), (0, '不启用')], default=0, verbose_name='是否启用'),
        ),
        migrations.AlterField(
            model_name='hotel_info',
            name='is_effective',
            field=models.IntegerField(choices=[(1, '启用'), (0, '不启用')], default=0, verbose_name='是否启用'),
        ),
        migrations.AlterField(
            model_name='room_image_info',
            name='imageLogo',
            field=models.IntegerField(choices=[(0, '有水印logo'), (-1, '未知'), (1, '无水印logo')], default=-1, verbose_name='是否带水印'),
        ),
        migrations.AlterField(
            model_name='room_image_info',
            name='imageSize',
            field=models.IntegerField(choices=[(0, '未分类'), (1, '350 * 350'), (3, '640 * 960'), (2, '550 * 412')], default=0, verbose_name='图片规格'),
        ),
        migrations.CreateModel(
            name='Hotel_Changed_Price',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='编号')),
                ('channel', models.CharField(default='未知', max_length=50, verbose_name='渠道')),
                ('changedPriceTime', models.DateTimeField(auto_now_add=True, verbose_name='请求时间')),
                ('changedPriceHotelList', models.CharField(max_length=2000, verbose_name='变价酒店')),
                ('sys_create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('sys_update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('sys_create_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
            ],
            options={
                'verbose_name': '变价时间表',
                'verbose_name_plural': '变价时间表',
                'db_table': 'hotel_changed_price',
                'managed': True,
            },
        ),
    ]
