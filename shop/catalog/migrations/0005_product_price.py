# Generated by Django 3.2.20 on 2023-08-14 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_product_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Цена товара'),
            preserve_default=False,
        ),
    ]
