# Generated by Django 5.0.4 on 2024-04-25 10:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('businessName', models.CharField(max_length=100)),
                ('businessCategory', models.CharField(blank=True, max_length=100, null=True)),
                ('businessRegistrationDate', models.DateField(blank=True, null=True)),
                ('ageOfBusiness', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerName', models.CharField(max_length=100)),
                ('phoneNumber', models.CharField(blank=True, max_length=20, null=True)),
                ('emailAddress', models.EmailField(blank=True, max_length=254, null=True)),
                ('dateOfBirth', models.DateField(blank=True, null=True)),
                ('nationality', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county', models.CharField(blank=True, max_length=50, null=True)),
                ('subCounty', models.CharField(blank=True, max_length=50, null=True)),
                ('ward', models.CharField(blank=True, max_length=50, null=True)),
                ('buildingName', models.CharField(blank=True, max_length=100, null=True)),
                ('floor', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerBusiness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.business')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customer')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.location')),
            ],
        ),
    ]