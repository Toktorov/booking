# Generated by Django 3.2.7 on 2022-02-22 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0005_alter_country_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='countryimage',
            options={'verbose_name': 'Фото города', 'verbose_name_plural': 'Фото городов'},
        ),
    ]
