# Generated by Django 3.0.8 on 2022-02-07 05:52

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Ticket', '0009_notif'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('slug', models.SlugField(blank=True, verbose_name='shortcut')),
                ('efforts', models.DurationField()),
                ('status', models.CharField(choices=[('1', 'Stuck'), ('2', 'Working'), ('3', 'Done')], default=1, max_length=7)),
                ('dead_line', models.DateField()),
                ('complete_per', models.FloatField(max_length=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('description', models.TextField(blank=True)),
                ('add_date', models.DateField(auto_now_add=True)),
                ('upd_date', models.DateField(auto_now=True)),
                ('assign', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('project_user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Project_users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
