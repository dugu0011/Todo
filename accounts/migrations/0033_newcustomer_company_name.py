# Generated by Django 3.0.8 on 2021-09-29 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0032_auto_20210923_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='newcustomer',
            name='company_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_newcustomer', to='accounts.Company'),
        ),
    ]