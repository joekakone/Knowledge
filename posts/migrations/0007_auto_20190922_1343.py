# Generated by Django 2.2.2 on 2019-09-22 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20190922_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(default='xxx', max_length=20),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(default='xxx', max_length=15),
        ),
        migrations.AlterField(
            model_name='author',
            name='number',
            field=models.CharField(default='XX-XX-XX-XX', max_length=25),
        ),
    ]
