# Generated by Django 3.2.18 on 2023-05-04 05:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicInformation',
            fields=[
                ('basic_information_id', models.AutoField(primary_key=True, serialize=False)),
                ('control_number', models.CharField(max_length=100, verbose_name='管理番号')),
                ('property_name', models.CharField(max_length=255, verbose_name='物件名')),
                ('location', models.CharField(max_length=255, verbose_name='所在地')),
                ('address', models.CharField(max_length=255, unique=True, verbose_name='住所地')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LandInformation',
            fields=[
                ('land_information_id', models.AutoField(primary_key=True, serialize=False)),
                ('area', models.FloatField(verbose_name='面積')),
                ('square_meter', models.FloatField(verbose_name='坪数')),
                ('land_category', models.IntegerField(verbose_name='地目')),
                ('certified_copy_of_land', models.CharField(max_length=100, verbose_name='土地謄本')),
                ('character_map', models.CharField(max_length=100, verbose_name='字図')),
                ('survey_map', models.CharField(max_length=100, verbose_name='測量図')),
                ('type_of_rights', models.CharField(max_length=100, verbose_name='権利の種類')),
                ('basic_information', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RealEstate360.basicinformation')),
            ],
        ),
        migrations.CreateModel(
            name='InfrastructureInformation',
            fields=[
                ('infrastructure_information_id', models.AutoField(primary_key=True, serialize=False)),
                ('water_supply', models.CharField(max_length=100, verbose_name='上水')),
                ('sweage', models.CharField(max_length=100, verbose_name='下水')),
                ('solar_power_generation', models.IntegerField(verbose_name='太陽光発電')),
                ('basic_information', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RealEstate360.basicinformation')),
            ],
        ),
        migrations.CreateModel(
            name='CityPlanning',
            fields=[
                ('city_planning_id', models.AutoField(primary_key=True, serialize=False)),
                ('zoning', models.CharField(max_length=100, verbose_name='用途地域')),
                ('public_land_expansion_act', models.CharField(max_length=100, verbose_name='公用地拡大法')),
                ('road_width', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='道路幅')),
                ('condition', models.CharField(max_length=100, verbose_name='状態')),
                ('basic_information', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RealEstate360.basicinformation')),
            ],
        ),
        migrations.CreateModel(
            name='BuildingInformation',
            fields=[
                ('building_information_id', models.AutoField(primary_key=True, serialize=False)),
                ('certified_copy_of_building', models.CharField(max_length=100, verbose_name='建物謄本取得')),
                ('building_drawing', models.CharField(max_length=100, verbose_name='')),
                ('building_confirmation_screen', models.CharField(max_length=100, verbose_name='建物図面取得')),
                ('property_tax_assessment_certificate', models.CharField(max_length=100, verbose_name='固定資産税評価証明書')),
                ('building_use', models.CharField(max_length=100, verbose_name='物件用途')),
                ('type_of_rights', models.CharField(max_length=100, verbose_name='新築年数')),
                ('relationship_to_land_owner', models.CharField(max_length=100, verbose_name='土地所有者との関係')),
                ('basic_information', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RealEstate360.basicinformation')),
            ],
        ),
    ]