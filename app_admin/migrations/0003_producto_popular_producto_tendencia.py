# Generated by Django 5.0.3 on 2024-03-30 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_admin', '0002_producto_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='popular',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='producto',
            name='tendencia',
            field=models.BooleanField(default=False),
        ),
    ]
