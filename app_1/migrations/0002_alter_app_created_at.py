# Generated by Django 4.0.6 on 2022-07-28 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created datetime'),
        ),
    ]