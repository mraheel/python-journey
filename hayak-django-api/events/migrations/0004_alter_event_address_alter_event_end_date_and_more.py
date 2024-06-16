# Generated by Django 5.0.6 on 2024-06-16 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_event_is_custom_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='address',
            field=models.CharField(default=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateField(default=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(default=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='guests',
            field=models.IntegerField(default=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='latitude',
            field=models.DecimalField(decimal_places=8, default=True, max_digits=10),
        ),
        migrations.AlterField(
            model_name='event',
            name='longitude',
            field=models.DecimalField(decimal_places=8, default=True, max_digits=11),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateField(default=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(default=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='event',
            name='tbd',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='timezone',
            field=models.CharField(default=True, max_length=30),
        ),
    ]
