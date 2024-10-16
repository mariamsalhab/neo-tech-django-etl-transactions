# Generated by Django 5.1.2 on 2024-10-12 19:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateField()),
                ('country', models.CharField(max_length=100)),
                ('account_balance', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('transaction_type', models.CharField(max_length=10)),
                ('transaction_date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(max_length=10)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.client')),
            ],
        ),
    ]
