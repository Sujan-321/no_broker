# Generated by Django 3.2.24 on 2024-10-29 07:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Residential', 'Residential'), ('Commercial', 'Commercial'), ('Land/Plot', 'Land/Plot')], max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=20)),
                ('property_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='owners.propertytype')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('address', models.TextField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='owners.city')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='owners.propertyoption')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to=settings.AUTH_USER_MODEL)),
                ('property_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='owners.propertytype')),
            ],
        ),
    ]
