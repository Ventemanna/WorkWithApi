# Generated by Django 5.2 on 2025-05-19 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_rename_address_id_supplier_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='available_stock',
            field=models.PositiveIntegerField(),
        ),
    ]
