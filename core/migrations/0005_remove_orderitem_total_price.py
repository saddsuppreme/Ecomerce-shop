# Generated by Django 4.0.3 on 2022-03-07 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_stash_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='total_price',
        ),
    ]
