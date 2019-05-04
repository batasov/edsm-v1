# Generated by Django 2.2 on 2019-05-03 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190504_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='adm',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='patronymic',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='position',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='second_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
