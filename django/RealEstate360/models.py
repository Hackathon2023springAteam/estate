from django.db import models
from django.db import models
from django.contrib.auth.models import User


class BasicInformation(models.Model):
    basic_information_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    control_number = models.CharField(max_length=100, unique=False, verbose_name="管理番号")
    property_name = models.CharField(max_length=255, unique=False, verbose_name="物件名")
    location = models.CharField(max_length=255, unique=False, verbose_name="所在地")
    address = models.CharField(max_length=255, unique=True, verbose_name="住所地")
    is_active = models.BooleanField(default=True, verbose_name="アクティブ")


class CityPlanning(models.Model):
    city_planning_id = models.AutoField(primary_key=True)
    basic_information = models.ForeignKey(BasicInformation, on_delete=models.CASCADE)
    zoning = models.CharField(max_length=100, unique=False, verbose_name="用途地域")
    public_land_expansion_act = models.CharField(
        max_length=100, unique=False, verbose_name="公用地拡大法"
    )
    road_width = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="道路幅")
    condition = models.CharField(max_length=100, unique=False, verbose_name="状態")


class BuildingInformation(models.Model):
    building_information_id = models.AutoField(primary_key=True)
    basic_information = models.ForeignKey(BasicInformation, on_delete=models.CASCADE)
    certified_copy_of_building = models.CharField(
        max_length=100, unique=False, verbose_name="建物謄本取得"
    )
    building_drawing = models.CharField(
        max_length=100, unique=False, verbose_name="建物図面取得"
    )
    building_confirmation_screen = models.CharField(
        max_length=100, unique=False, verbose_name="建物確認図面"
    )
    property_tax_assessment_certificate = models.CharField(
        max_length=100, unique=False, verbose_name="固定資産税評価証明書"
    )
    building_use = models.CharField(max_length=100, unique=False, verbose_name="物件用途")
    type_of_rights = models.CharField(max_length=100, unique=False, verbose_name="新築年数")
    relationship_to_land_owner = models.CharField(
        max_length=100, unique=False, verbose_name="土地所有者との関係"
    )


class LandInformation(models.Model):
    land_information_id = models.AutoField(primary_key=True)
    basic_information = models.ForeignKey(BasicInformation, on_delete=models.CASCADE)
    area = models.FloatField(verbose_name="面積")
    square_meter = models.FloatField(verbose_name="坪数")
    land_category = models.IntegerField(verbose_name="地目")
    certified_copy_of_land = models.CharField(
        max_length=100, unique=False, verbose_name="土地謄本"
    )
    character_map = models.CharField(max_length=100, unique=False, verbose_name="字図")
    survey_map = models.CharField(max_length=100, unique=False, verbose_name="測量図")
    type_of_rights = models.CharField(
        max_length=100, unique=False, verbose_name="権利の種類"
    )


class InfrastructureInformation(models.Model):
    infrastructure_information_id = models.AutoField(primary_key=True)
    basic_information = models.ForeignKey(BasicInformation, on_delete=models.CASCADE)
    water_supply = models.CharField(max_length=100, unique=False, verbose_name="上水")
    sweage = models.CharField(max_length=100, unique=False, verbose_name="下水")
    solar_power_generation = models.IntegerField(verbose_name="太陽光発電")
