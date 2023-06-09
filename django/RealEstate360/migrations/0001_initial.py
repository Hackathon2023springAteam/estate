# Generated by Django 3.2.18 on 2023-05-23 04:04

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicInformation',
            fields=[
                ('basic_information_id', models.AutoField(primary_key=True, serialize=False)),
                ('control_number', models.CharField(blank=True, max_length=100, verbose_name='管理番号')),
                ('property_name', models.CharField(max_length=255, verbose_name='物件名')),
                ('location', models.CharField(max_length=255, verbose_name='所在地')),
                ('address', models.CharField(max_length=255, verbose_name='住所地')),
                ('is_active', models.BooleanField(default=True, verbose_name='アクティブ')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='LandInformation',
            fields=[
                ('land_information_id', models.AutoField(primary_key=True, serialize=False)),
                ('area', models.FloatField(verbose_name='面積(平米)')),
                ('square_meter', models.FloatField(verbose_name='面積(坪)')),
                ('land_category', models.CharField(max_length=100, verbose_name='地目')),
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
                ('solar_power_generation', models.IntegerField(verbose_name='太陽光発電(kW)')),
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
                ('building_drawing', models.CharField(max_length=100, verbose_name='建物図面取得')),
                ('building_confirmation_screen', models.CharField(max_length=100, verbose_name='建物確認図面')),
                ('property_tax_assessment_certificate', models.CharField(max_length=100, verbose_name='固定資産税評価証明書')),
                ('building_use', models.CharField(max_length=100, verbose_name='物件用途')),
                ('type_of_rights', models.CharField(max_length=100, verbose_name='権利の種類')),
                ('relationship_to_land_owner', models.CharField(max_length=100, verbose_name='土地所有者との関係')),
                ('basic_information', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RealEstate360.basicinformation')),
            ],
        ),
        migrations.AddField(
            model_name='basicinformation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
