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
                ('goods_specs', models.CharField(max_length=255, verbose_name='Goods Specs')),
                ('creater', models.CharField(max_length=255, verbose_name='Who created')),
                ('openid', models.CharField(max_length=255, verbose_name='Openid')),
                ('is_delete', models.BooleanField(default=False, verbose_name='Delete Label')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create Time')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Update Time')),
            ],
            options={
                'verbose_name': 'Goods Specs',
                'verbose_name_plural': 'Goods Specs',
                'db_table': 'goodsspecs',
                'ordering': ['goods_specs'],
            },
        ),
    ]
