# Generated by Django 4.1.2 on 2024-09-19 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warehouse_name', models.CharField(max_length=255, verbose_name='Warehouse Name')),
                ('warehouse_city', models.CharField(max_length=255, verbose_name='Warehouse City')),
                ('warehouse_address', models.CharField(max_length=255, verbose_name='Warehouse Address')),
                ('warehouse_contact', models.CharField(max_length=255, verbose_name='Warehouse Contact')),
                ('warehouse_manager', models.CharField(max_length=255, verbose_name='Warehouse Manager')),
                ('creater', models.CharField(max_length=255, verbose_name='Who Created')),
                ('openid', models.CharField(max_length=255, verbose_name='Openid')),
                ('is_delete', models.BooleanField(default=False, verbose_name='Delete Label')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create Time')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Update Time')),
            ],
            options={
                'verbose_name': 'Warehouse',
                'verbose_name_plural': 'Warehouse',
                'db_table': 'warehouse',
                'ordering': ['-id'],
            },
        ),
    ]
