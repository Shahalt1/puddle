# Generated by Django 5.1 on 2024-10-28 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_item_category_item_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('name',), 'verbose_name_plural': 'Items'},
        ),
    ]