# Generated by Django 2.2.7 on 2019-12-06 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
