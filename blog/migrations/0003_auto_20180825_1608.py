# Generated by Django 2.1 on 2018-08-25 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180823_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.TextField(max_length=1024),
        ),
    ]
