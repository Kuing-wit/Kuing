# Generated by Django 3.0.8 on 2020-08-29 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Building_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(default='', max_length=10),
        ),
    ]
