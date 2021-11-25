# Generated by Django 3.2.7 on 2021-11-25 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firsttry', '0014_ask_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ask',
            name='user',
            field=models.CharField(max_length=50, null=True, verbose_name='Имя отправителя'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='dir_way',
            field=models.FileField(upload_to='images/', verbose_name='Файл'),
        ),
    ]
