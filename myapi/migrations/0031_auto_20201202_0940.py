# Generated by Django 3.1.3 on 2020-12-02 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0030_medico_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='subtotal',
            new_name='precio',
        ),
        migrations.AddField(
            model_name='pedido',
            name='paciente',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='myapi.paciente'),
            preserve_default=False,
        ),
    ]
