# Generated by Django 3.1.3 on 2020-12-01 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0027_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='clave',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre_usuario',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.CharField(max_length=30),
        ),
    ]
