# Generated by Django 3.2.7 on 2021-09-25 04:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0009_auto_20210921_2320'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0018_auto_20210924_2234'),
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
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.user'),
            preserve_default=False,
        ),
    ]
