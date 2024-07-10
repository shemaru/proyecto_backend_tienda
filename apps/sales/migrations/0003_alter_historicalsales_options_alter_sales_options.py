# Generated by Django 5.0.6 on 2024-07-10 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalsales',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Venta', 'verbose_name_plural': 'historical Ventas'},
        ),
        migrations.AlterModelOptions(
            name='sales',
            options={'verbose_name': 'Venta', 'verbose_name_plural': 'Ventas'},
        ),
    ]