# Generated by Django 3.2.2 on 2021-05-15 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurante', '0012_remove_pedido_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='total',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
