# Generated by Django 3.0.8 on 2021-09-09 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20210909_2130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='last_name',
        ),
        migrations.AddField(
            model_name='myuser',
            name='gender',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='mobile',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
