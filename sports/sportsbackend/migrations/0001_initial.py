# Generated by Django 2.1.5 on 2019-02-12 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Participate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(choices=[(0, 'Registered'), (1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fourth'), (5, 'Participated'), (6, 'University'), (7, 'District'), (8, 'State'), (9, 'National'), (10, 'International')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('selected', models.BooleanField(default=False)),
            ],
        ),
    ]
