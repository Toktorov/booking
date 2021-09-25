# Generated by Django 3.2.7 on 2021-09-25 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0009_auto_20210921_2320'),
        ('orders', '0008_auto_20210924_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='hotels.hotel'),
        ),
    ]