# Generated by Django 3.1.3 on 2020-12-01 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0025_auto_20201130_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='subtotal',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
