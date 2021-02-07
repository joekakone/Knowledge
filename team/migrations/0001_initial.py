# Generated by Django 2.2.2 on 2019-10-18 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.CharField(default='00228 96273390', max_length=15)),
                ('message', models.TextField()),
                ('profile_picture', models.ImageField(upload_to='')),
                ('roles', models.ManyToManyField(to='team.Role')),
            ],
        ),
    ]
