# Generated by Django 2.2.2 on 2019-10-18 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_member_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='description',
            field=models.TextField(default='Pellentesque habitant morbi tristique senectus\t\tet netus et malesuada fames ac turpis egestas.'),
        ),
    ]
