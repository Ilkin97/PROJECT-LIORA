# Generated by Django 5.1.5 on 2025-01-26 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0003_product_volume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='volume',
            field=models.CharField(choices=[('50ml', '50ml'), ('100ml', '100ml')], max_length=5),
        ),
    ]
