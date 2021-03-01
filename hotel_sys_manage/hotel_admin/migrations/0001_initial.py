# Generated by Django 2.2 on 2021-02-28 20:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel_info',
            fields=[
                ('hotel_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='无', max_length=100, verbose_name='名称')),
                ('city', models.CharField(default='未知', max_length=50, verbose_name='城市')),
                ('address', models.CharField(default='未知', max_length=200, verbose_name='地址')),
                ('sys_create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('sys_update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('sys_create_user',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL,
                                   verbose_name='创建人')),
            ],
            options={
                'verbose_name': '酒店信息表',
                'verbose_name_plural': '酒店信息表',
                'db_table': 'hotel_info',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Price_model_info',
            fields=[
                ('price_model_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='无', max_length=100, verbose_name='名称')),
                ('proportion', models.DecimalField(decimal_places=2, default=1.0, max_digits=5, verbose_name='加价比列')),
                ('level',
                 models.IntegerField(choices=[('2', '自定义'), ('1', '节假日'), ('0', '默认'), ('9', '最高级')], default=0,
                                     verbose_name='优先级')),
            ],
            options={
                'verbose_name': '加价类型表',
                'verbose_name_plural': '加价类型表',
                'db_table': 'price_model_info',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Room_info',
            fields=[
                ('room_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('room_type', models.CharField(default='无', max_length=100, verbose_name='房型')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='报价')),
                ('custom_proce',
                 models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='强制自定义售价')),
                ('sys_create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('sys_update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('hotel',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hotel_admin.Hotel_info',
                                   verbose_name='酒店')),
                ('price_model', models.ManyToManyField(to='hotel_admin.Price_model_info', verbose_name='加价类型')),
                ('sys_create_user',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL,
                                   verbose_name='创建人')),
            ],
            options={
                'verbose_name': '房间信息表',
                'verbose_name_plural': '房间信息表',
                'db_table': 'room_info',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Order_info',
            fields=[
                ('order_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('room_type', models.CharField(default='无', max_length=100, verbose_name='房型')),
                ('channel', models.CharField(max_length=100, verbose_name='渠道')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='报价')),
                ('custom_proce',
                 models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='强制自定义售价')),
                ('sys_create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('sys_update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('hotel',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hotel_admin.Hotel_info',
                                   verbose_name='酒店')),
                ('price_model', models.ManyToManyField(to='hotel_admin.Price_model_info', verbose_name='加价类型')),
                ('sys_create_user',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL,
                                   verbose_name='创建人')),
            ],
            options={
                'verbose_name': '订单信息',
                'verbose_name_plural': '订单信息',
                'db_table': 'order_info',
                'managed': True,
            },
        ),
    ]