# Generated by Django 3.2.7 on 2021-10-03 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0002_rename_servicios_servicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='imagen',
            field=models.ImageField(upload_to='sevicios'),
        ),
    ]