# Generated by Django 3.2.2 on 2021-05-15 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0010_pedido_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]
