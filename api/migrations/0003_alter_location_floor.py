# Generated by Django 5.0.4 on 2024-04-25 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_customerbusiness_customerbusinesslocation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='floor',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
