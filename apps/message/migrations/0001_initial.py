# Generated by Django 2.0.2 on 2018-03-08 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='用户名')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('address', models.CharField(max_length=30, verbose_name='地址')),
                ('message', models.TextField(max_length=200, verbose_name='信息')),
            ],
            options={
                'verbose_name': '用户留言信息',
            },
        ),
    ]
