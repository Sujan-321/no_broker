# Generated by Django 3.2.24 on 2024-10-31 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owners', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='property',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='property',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='option',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='property',
            name='owner',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_type',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='RentalDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_type', models.CharField(choices=[('Rent', 'Only Rent'), ('Lease', 'Only Lease')], max_length=10)),
                ('expected_rent', models.FloatField(blank=True, null=True)),
                ('expected_lease_amount', models.FloatField(blank=True, null=True)),
                ('expected_deposit', models.FloatField(blank=True, null=True)),
                ('monthly_maintenance', models.CharField(blank=True, max_length=20, null=True)),
                ('available_from', models.DateField(blank=True, null=True)),
                ('preferred_tenants', models.CharField(blank=True, max_length=50, null=True)),
                ('furnishing', models.CharField(blank=True, max_length=20, null=True)),
                ('parking', models.CharField(blank=True, max_length=20, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('property', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='rental', to='owners.property')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartment_type', models.CharField(blank=True, max_length=50, null=True)),
                ('apartment_name', models.CharField(blank=True, max_length=100, null=True)),
                ('bhk_type', models.CharField(blank=True, max_length=10, null=True)),
                ('floor', models.IntegerField(blank=True, null=True)),
                ('total_floor', models.IntegerField(blank=True, null=True)),
                ('property_age', models.CharField(blank=True, max_length=20, null=True)),
                ('facing', models.CharField(blank=True, max_length=20, null=True)),
                ('built_up_area', models.FloatField(blank=True, null=True)),
                ('property', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='owners.property')),
            ],
        ),
        migrations.CreateModel(
            name='LocalityDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locality', models.CharField(blank=True, max_length=100, null=True)),
                ('landmark', models.CharField(blank=True, max_length=100, null=True)),
                ('property', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='locality', to='owners.property')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_images', models.JSONField(blank=True, null=True)),
                ('property', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='owners.property')),
            ],
        ),
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bathrooms', models.IntegerField(blank=True, null=True)),
                ('balcony', models.BooleanField(default=False)),
                ('water_supply', models.CharField(blank=True, max_length=20, null=True)),
                ('gym', models.BooleanField(default=False)),
                ('non_veg', models.BooleanField(default=False)),
                ('gated_security', models.BooleanField(default=False)),
                ('show_property_by', models.CharField(blank=True, max_length=50, null=True)),
                ('secondary_number', models.CharField(blank=True, max_length=15, null=True)),
                ('similar_units_available', models.BooleanField(default=False)),
                ('directions_tip', models.TextField(blank=True, null=True)),
                ('property', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='amenities', to='owners.property')),
            ],
        ),
    ]