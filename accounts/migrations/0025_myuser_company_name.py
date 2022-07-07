# Generated by Django 3.0.8 on 2021-09-17 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_auto_20210916_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='company_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='myuser_company', to='accounts.Company'),
        ),
    ]
