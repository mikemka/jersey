# Generated by Django 3.2.20 on 2023-08-13 20:30

from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, unique=True, verbose_name='Название товара')),
                ('thumbnail', sorl.thumbnail.fields.ImageField(default=None, null=True, upload_to='uploads/', verbose_name='Изображение товара')),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', sorl.thumbnail.fields.ImageField(default=None, null=True, upload_to='uploads/', verbose_name='Дополнительное изображение товара')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'изображение',
                'verbose_name_plural': 'изображения',
            },
        ),
    ]
