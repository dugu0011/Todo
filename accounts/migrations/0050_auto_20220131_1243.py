# Generated by Django 3.0.8 on 2022-01-31 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0049_merge_20220104_1704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='powerfactor',
            old_name='Added_by',
            new_name='added_by',
        ),
        migrations.AddField(
            model_name='hsncode',
            name='percentage',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True),
        ),
        migrations.AddField(
            model_name='powerfactor',
            name='dailykvah',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='powerfactor',
            name='dailykwh',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='powerfactor',
            name='dailypower',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='productmaster',
            name='is_gst',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_type',
            field=models.CharField(choices=[('kaata', 'Kaata'), ('client', 'Client'), ('vendor', 'Vendor'), ('mine', 'Mine'), ('crusher', 'Crusher'), ('minecrusher', 'Mine&Crusher'), ('contractor', 'Contractor'), ('transporter', 'Transporter'), ('individual', 'Individual'), ('properitor', 'Properitor'), ('partner', 'Partner'), ('llp', 'LLP'), ('pvt_ltd', 'PVT LTD'), ('ltd', 'LTD')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='customer_category',
            field=models.CharField(choices=[('kaata', 'Kaata'), ('client', 'Client'), ('vendor', 'Vendor'), ('mine', 'Mine'), ('crusher', 'Crusher'), ('minecrusher', 'Mine&Crusher'), ('contractor', 'Contractor'), ('transporter', 'Transporter'), ('individual', 'Individual'), ('properitor', 'Properitor'), ('partner', 'Partner'), ('llp', 'LLP'), ('pvt_ltd', 'PVT LTD'), ('ltd', 'LTD')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='newcustomer',
            name='customer_type',
            field=models.CharField(choices=[('kaata', 'Kaata'), ('client', 'Client'), ('vendor', 'Vendor'), ('mine', 'Mine'), ('crusher', 'Crusher'), ('minecrusher', 'Mine&Crusher'), ('contractor', 'Contractor'), ('transporter', 'Transporter'), ('individual', 'Individual'), ('properitor', 'Properitor'), ('partner', 'Partner'), ('llp', 'LLP'), ('pvt_ltd', 'PVT LTD'), ('ltd', 'LTD')], max_length=50, null=True),
        ),
    ]