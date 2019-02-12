# Generated by Django 2.1.5 on 2019-02-12 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
        ('sportsbackend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participate',
            name='cno',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.ChestNo'),
        ),
        migrations.AddField(
            model_name='participate',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sportsbackend.Event'),
        ),
        migrations.AddField(
            model_name='participate',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
        ),
        migrations.AddField(
            model_name='participate',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sportsbackend.Year'),
        ),
    ]