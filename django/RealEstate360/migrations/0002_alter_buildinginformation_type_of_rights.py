# Generated by Django 3.2.18 on 2023-05-16 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RealEstate360', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildinginformation',
            name='type_of_rights',
            field=models.CharField(max_length=100, verbose_name='権利の種類'),
        ),
    ]