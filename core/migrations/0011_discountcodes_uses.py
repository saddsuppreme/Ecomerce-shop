# Generated by Django 4.0.3 on 2022-03-12 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_rename_body_discountcodes_code_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='discountcodes',
            name='uses',
            field=models.IntegerField(default=1),
        ),
    ]
