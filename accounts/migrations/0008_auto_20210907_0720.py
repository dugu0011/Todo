# Generated by Django 3.0.8 on 2021-09-07 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210907_0715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newcustomer',
            name='customer_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='gst_no',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='mobile',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_customer', to='accounts.NewCustomer'),
        ),
    ]
