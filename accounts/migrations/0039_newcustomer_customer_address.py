# Generated by Django 3.0.8 on 2021-10-08 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0038_auto_20211006_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='newcustomer',
            name='customer_address',
            field=models.ManyToManyField(blank=True, to='accounts.Address'),
        ),
    ]