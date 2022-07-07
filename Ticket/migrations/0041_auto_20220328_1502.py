# Generated by Django 3.0.8 on 2022-03-28 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ticket', '0040_auto_20220328_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raiseticket',
            name='msg',
            field=models.TextField(max_length=800),
        ),
        migrations.AlterField(
            model_name='raiseticket',
            name='priority',
            field=models.CharField(choices=[('High', 'High'), ('Low', 'Low'), ('Medium', 'Medium')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='raiseticket',
            name='subcategory',
            field=models.CharField(choices=[('CNM', 'CNM'), ('CNM58', 'CNM58'), ('ULTRACON', 'ULTRACON'), ('TECH58', 'TECH58'), ('HR58', 'HR58')], max_length=50, null=True),
        ),
    ]