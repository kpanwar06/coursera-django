# Generated by Django 5.1.2 on 2024-10-24 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_cake_order_cake_flavour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cake_order',
            name='cake_flavour',
            field=models.IntegerField(choices=[(1, 'Chocolate'), (2, 'Strawberry'), (3, 'Vanilla')]),
        ),
    ]
