# Generated by Django 2.2.7 on 2019-12-08 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_users_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
