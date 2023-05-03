from django.db import models
from django.db import models
from django.contrib.auth.models import User


class BasicInformation(models.Model):
    basic_information_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    control_number = models.CharField(max_length=100, unique=False)
    property_name = models.CharField(max_length=255, unique=False)
    location = models.CharField(max_length=255, unique=False)
    address = models.CharField(max_length=255, unique=True)


class CityPlanning(models.Model):
    city_planning_id = models.AutoField(primary_key=True)
    basic_information = models.ForeignKey(BasicInformation, on_delete=models.CASCADE)
    zoning = models.CharField(max_length=100, unique=False)
    public_land_expansion_act = models.CharField(max_length=100, unique=False)
    road_width = models.DecimalField(max_digits=3, decimal_places=1)
    condition = models.CharField(max_length=100, unique=False)


class BuildingInformation(models.Model):
    building_information_id = models.AutoField(primary_key=True)
    basic_information = models.ForeignKey(BasicInformation, on_delete=models.CASCADE)
    certified_copy_of_building = models.CharField(max_length=100, unique=False)
    building_drawing = models.CharField(max_length=100, unique=False)
    building_confirmation_screen = models.CharField(max_length=100, unique=False)
    property_tax_assessment_certificate = models.CharField(max_length=100, unique=False)
    building_use = models.CharField(max_length=100, unique=False)
    type_of_rights = models.CharField(max_length=100, unique=False)
    relationship_to_land_owner = models.CharField(max_length=100, unique=False)


class LandInformation(models.Model):
    land_information_id = models.AutoField(primary_key=True)
    basic_information = models.ForeignKey(BasicInformation, on_delete=models.CASCADE)
    area = models.FloatField()
    square_meter = models.FloatField()
    land_category = models.IntegerField()
    certified_copy_of_land = models.CharField(max_length=100, unique=False)
    character_map = models.CharField(max_length=100, unique=False)
    survey_map = models.CharField(max_length=100, unique=False)
    type_of_rights = models.CharField(max_length=100, unique=False)


class InfrastructureInformation(models.Model):
    infrastructure_information_id = models.AutoField(primary_key=True)
    basic_information = models.ForeignKey(BasicInformation, on_delete=models.CASCADE)
    water_supply = models.CharField(max_length=100, unique=False)
    sweage = models.CharField(max_length=100, unique=False)
    solar_power_generation = models.IntegerField()
