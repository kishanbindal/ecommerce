# Generated by Django 3.0.3 on 2020-06-12 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0007_orderproduct_is_billed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]