# Generated by Django 4.0.4 on 2022-05-02 04:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='promotions',
            field=models.ManyToManyField(blank=True, to='store.promotion'),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]