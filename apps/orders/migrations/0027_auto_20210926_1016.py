# Generated by Django 3.2.7 on 2021-09-26 16:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0009_auto_20210921_2320'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0026_auto_20210924_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='hotels.hotel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='users.user'),
            preserve_default=False,
        ),
    ]
