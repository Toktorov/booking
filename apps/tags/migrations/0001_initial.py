# Generated by Django 3.2.7 on 2021-09-21 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('hotels', models.ManyToManyField(to='hotels.Hotel')),
            ],
            options={
                'verbose_name': 'Теги',
                'verbose_name_plural': 'Теги',
                'ordering': ('-id',),
            },
        ),
    ]
