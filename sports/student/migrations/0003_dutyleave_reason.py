# Generated by Django 2.1.5 on 2019-02-26 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20190214_0354'),
    ]

    operations = [
        migrations.AddField(
            model_name='dutyleave',
            name='reason',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
