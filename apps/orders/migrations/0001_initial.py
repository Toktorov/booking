# Generated by Django 3.2.7 on 2021-09-21 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('arrival_date', models.DateTimeField(verbose_name='Дата заезда:')),
                ('departure_date', models.DateTimeField(verbose_name='Дата отъезда:')),
                ('name', models.CharField(max_length=50, verbose_name='Имя:')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия:')),
                ('fatherland', models.CharField(max_length=50, verbose_name='Отечество:')),
                ('id_card', models.CharField(max_length=50, verbose_name='Паспорт:')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='hotels.hotel')),
            ],
            options={
                'verbose_name': 'Брони',
                'verbose_name_plural': 'Брони',
                'ordering': ('-create_at',),
            },
        ),
    ]
