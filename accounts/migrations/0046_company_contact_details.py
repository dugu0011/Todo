# Generated by Django 3.0.8 on 2021-11-25 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0045_auto_20211119_2314'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='contact_details',
            field=models.ManyToManyField(blank=True, related_name='contact_to', to='accounts.ContactDetail'),
        ),
    ]
