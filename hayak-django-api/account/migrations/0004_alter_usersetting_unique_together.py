# Generated by Django 5.0.6 on 2024-06-13 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_usersetting'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='usersetting',
            unique_together={('user', 'key')},
        ),
    ]
