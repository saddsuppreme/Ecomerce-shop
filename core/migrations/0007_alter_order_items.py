# Generated by Django 4.0.3 on 2022-03-09 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_order_code_order_country_order_email_order_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='core.orderitem'),
        ),
    ]
