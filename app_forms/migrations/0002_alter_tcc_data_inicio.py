# Generated by Django 5.1.3 on 2024-11-30 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_forms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tcc',
            name='data_inicio',
            field=models.DateField(),
        ),
    ]
