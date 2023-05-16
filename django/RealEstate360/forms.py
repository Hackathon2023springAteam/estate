from django import forms
from .models import (
    BasicInformation,
    CityPlanning,
    BuildingInformation,
    LandInformation,
    InfrastructureInformation,
)

# 基本情報
class BasicInformationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BasicInformationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"autocomplete": "off"})
        # 管理番号
        self.fields["control_number"].widget = forms.TextInput(attrs={'class': 'form-control'})
        # 物件名
        self.fields["property_name"].widget = forms.TextInput(attrs={'class': 'form-control'})
        # 所在地
        self.fields["location"].widget = forms.TextInput(attrs={'class': 'form-control'})
        # 住所地
        self.fields["address"].widget = forms.TextInput(attrs={'class': 'form-control'})

    def save(self, commit=True):
        instance = super(BasicInformationForm, self).save(commit=False)
        instance.control_number = self.cleaned_data["control_number"]
        instance.property_name = self.cleaned_data["property_name"]
        instance.location = self.cleaned_data["location"]
        instance.address = self.cleaned_data["address"]

        if commit:
            instance.save()
        return instance

    class Meta:
        model = BasicInformation
        fields = [
            "control_number",
            "property_name",
            "location",
            "address",
        ]

# 都市計画
class CityPlanningForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CityPlanningForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"autocomplete": "off"})
        # 用途地域
        self.fields["zoning"].widget = forms.TextInput(attrs={'class': 'form-control'})
        # 公用地拡大法
        self.fields["public_land_expansion_act"].widget = forms.TextInput(attrs={'class': 'form-control'})
        # 道路幅
        self.fields["road_width"].widget = forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'})
        # 状態
        self.fields["condition"].widget = forms.TextInput(attrs={'class': 'form-control'})

    def save(self, commit=True):
        instance = super(CityPlanningForm, self).save(commit=False)
        instance.zoning = self.cleaned_data["zoning"]
        instance.public_land_expansion_act = self.cleaned_data[
            "public_land_expansion_act"
        ]
        instance.road_width = self.cleaned_data["road_width"]
        instance.condition = self.cleaned_data["condition"]

        if commit:
            instance.save()
        return instance

    class Meta:
        model = CityPlanning
        fields = [
            "zoning",
            "public_land_expansion_act",
            "road_width",
            "condition",
        ]

# 建物情報
class BuildingInformationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BuildingInformationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"autocomplete": "off"})
        # 建物謄本取得
        self.fields["certified_copy_of_building"].widget = forms.TextInput(attrs={'class': 'form-control'})
        # 建物図面取得
        self.fields["building_drawing"].widget = forms.TextInput(attrs={'class': 'form-control'})
        # 建物確認図面
        self.fields["building_confirmation_screen"].widget = forms.TextInput(attrs={'class': 'form-control'})
        # 固定資産税評価証明書
        self.fields["property_tax_assessment_certificate"].widget = forms.TextInput(attrs={'class': 'form-control'})
        # 物件用途
        self.fields["building_use"].widget = forms.TextInput(attrs={'class': 'form-control'})
        # 新築年数
        self.fields["type_of_rights"].widget = forms.TextInput(attrs={'class': 'form-control'})
        # 土地所有者との関係
        self.fields["relationship_to_land_owner"].widget = forms.TextInput(attrs={'class': 'form-control'})

    def save(self, commit=True):
        instance = super(BuildingInformationForm, self).save(commit=False)
        instance.certified_copy_of_building = self.cleaned_data[
            "certified_copy_of_building"
        ]
        instance.building_drawing = self.cleaned_data["building_drawing"]
        instance.building_confirmation_screen = self.cleaned_data[
            "building_confirmation_screen"
        ]
        instance.property_tax_assessment_certificate = self.cleaned_data[
            "property_tax_assessment_certificate"
        ]
        instance.building_use = self.cleaned_data["building_use"]
        instance.type_of_rights = self.cleaned_data["type_of_rights"]
        instance.relationship_to_land_owner = self.cleaned_data[
            "relationship_to_land_owner"
        ]

        if commit:
            instance.save()
        return instance

    class Meta:
        model = BuildingInformation
        fields = [
            "certified_copy_of_building",
            "building_drawing",
            "building_confirmation_screen",
            "property_tax_assessment_certificate",
            "building_use",
            "type_of_rights",
            "relationship_to_land_owner",
        ]

# 土地情報
class LandInformationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LandInformationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"autocomplete": "off"})
        # 面積
        self.fields["area"].widget = forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'})
        # 坪数
        self.fields["square_meter"].widget = forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'})
        # 地目
        self.fields["land_category"].widget = forms.NumberInput(attrs={'class': 'form-control', 'step': '1'})
        # 土地謄本
        self.fields["certified_copy_of_land"].widget = forms.TextInput(attrs={'class': 'form-control'})
        # 字図
        self.fields["character_map"].widget = forms.TextInput(attrs={'class': 'form-control'})
        # 測量図
        self.fields["survey_map"].widget = forms.TextInput(attrs={'class': 'form-control'})
        # 権利の種類
        self.fields["type_of_rights"].widget = forms.TextInput(attrs={'class': 'form-control'})

    def save(self, commit=True):
        instance = super(LandInformationForm, self).save(commit=False)
        instance.area = self.cleaned_data["area"]
        instance.square_meter = self.cleaned_data["square_meter"]
        instance.land_category = self.cleaned_data["land_category"]
        instance.certified_copy_of_land = self.cleaned_data["certified_copy_of_land"]
        instance.character_map = self.cleaned_data["character_map"]
        instance.survey_map = self.cleaned_data["survey_map"]
        instance.type_of_rights = self.cleaned_data["type_of_rights"]

        if commit:
            instance.save()
        return instance

    class Meta:
        model = LandInformation
        fields = [
            "area",
            "square_meter",
            "land_category",
            "certified_copy_of_land",
            "character_map",
            "survey_map",
            "type_of_rights",
        ]

# インフラ情報
class InfrastructureInformationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InfrastructureInformationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"autocomplete": "off"})
        # 上水
        self.fields["water_supply"].widget = forms.TextInput(attrs={'class': 'form-control'})
        # 下水
        self.fields["sweage"].widget = forms.TextInput(attrs={'class': 'form-control'})
        # 太陽光発電
        self.fields["solar_power_generation"].widget = forms.NumberInput(attrs={'class': 'form-control', 'step': '1'})


    def save(self, commit=True):
        instance = super(InfrastructureInformationForm, self).save(commit=False)
        instance.water_supply = self.cleaned_data["water_supply"]
        instance.sweage = self.cleaned_data["sweage"]
        instance.solar_power_generation = self.cleaned_data["solar_power_generation"]

        if commit:
            instance.save()
        return instance

    class Meta:
        model = InfrastructureInformation
        fields = [
            "water_supply",
            "sweage",
            "solar_power_generation",
        ]
