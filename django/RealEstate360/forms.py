from django import forms
from .models import (
    BasicInformation,
    CityPlanning,
    BuildingInformation,
    LandInformation,
    InfrastructureInformation,
)


class BasicInformationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BasicInformationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"autocomplete": "off"})

        self.fields["control_number"].widget = forms.TextInput(
            attrs={"class": "form-control"}
        )
        self.fields["property_name"].widget = forms.TextInput(
            attrs={"class": "form-control"}
        )
        self.fields["location"].widget = forms.TextInput(
            attrs={"class": "form-control"}
        )
        self.fields["address"].widget = forms.TextInput(attrs={"class": "form-control"})

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


class CityPlanningForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CityPlanningForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"autocomplete": "off"})

        self.fields["zoning"].widget = forms.Select(
            attrs={"class": "form-control"},
            choices=[
                ("選択してください", "選択してください"),
                ("第一種低層住居専用地域", "第一種低層住居専用地域"),
                ("第二種低層住居専用地域", "第二種低層住居専用地域"),
                ("第一種中高層住居専用地域", "第一種中高層住居専用地域"),
                ("第二種中高層住居専用地域", "第二種中高層住居専用地域"),
                ("第一種住居地域", "第一種住居地域"),
                ("第二種住居地域", "第二種住居地域"),
                ("準住居地域", "準住居地域"),
                ("田園住居地域", "田園住居地域"),
                ("近隣商業地域", "近隣商業地域"),
                ("商業地域", "商業地域"),
                ("準工業地域", "準工業地域"),
                ("工業地域", "工業地域"),
                ("工業専用地域", "工業専用地域"),
            ],
        )
        self.fields["public_land_expansion_act"].widget = forms.Select(
            attrs={"class": "form-control"},
            choices=[
                ("選択してください", "選択してください"),
                ("有", "あり"),
                ("無", "なし"),
                ("未調査", "未調査"),
            ],
        )
        self.fields["road_width"].widget = forms.NumberInput(
            attrs={
                "class": "form-control",
                "step": "0.1",
                "min": "0",
            }
        )
        self.fields["condition"].widget = forms.Select(
            attrs={"class": "form-control"},
            choices=[
                ("選択してください", "選択してください"),
                ("空家", "空家"),
                ("空き地", "空き地"),
                ("居住中", "居住中"),
                ("その他", "その他"),
            ],
        )

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


class BuildingInformationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BuildingInformationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"autocomplete": "off"})

        self.fields["certified_copy_of_building"].widget = forms.Select(
            attrs={"class": "form-control"},
            choices=[
                ("選択してください", "選択してください"),
                ("取得", "取得"),
                ("未取得", "未取得"),
                ("登記なし", "登記なし"),
                ("税務登録のみ", "税務登録のみ"),
            ],
        )
        self.fields["building_drawing"].widget = forms.Select(
            attrs={"class": "form-control"},
            choices=[
                ("選択してください", "選択してください"),
                ("取得", "取得"),
                ("未取得", "未取得"),
                ("存在なし", "存在なし"),
                ("未調査", "未調査"),
            ],
        )
        self.fields["building_confirmation_screen"].widget = forms.Select(
            attrs={"class": "form-control"},
            choices=[
                ("選択してください", "選択してください"),
                ("取得", "取得"),
                ("未取得", "未取得"),
                ("存在なし", "存在なし"),
                ("未調査", "未調査"),
            ],
        )
        self.fields["property_tax_assessment_certificate"].widget = forms.Select(
            attrs={"class": "form-control"},
            choices=[
                ("選択してください", "選択してください"),
                ("取得", "取得"),
                ("未取得", "未取得"),
                ("存在なし", "存在なし"),
                ("未調査", "未調査"),
            ],
        )
        self.fields["building_use"].widget = forms.Select(
            attrs={"class": "form-control"},
            choices=[
                ("選択してください", "選択してください"),
                ("居宅", "居宅"),
                ("店舗", "店舗"),
                ("寄宿舎", "寄宿舎"),
                ("共同住宅", "共同住宅"),
                ("事務所", "事務所"),
                ("旅館", "旅館"),
                ("料理店", "料理店"),
                ("工場", "工場"),
                ("倉庫", "倉庫"),
                ("車庫", "車庫"),
                ("発電所", "発電所"),
                ("変電所", "変電所"),
            ],
        )
        self.fields["type_of_rights"].widget = forms.Select(
            attrs={"class": "form-control"},
            choices=[
                ("選択してください", "選択してください"),
                ("所有権", "所有権"),
                ("敷地権", "敷地権"),
                ("地上権", "地上権"),
                ("借地権", "借地権"),
            ],
        )
        self.fields["relationship_to_land_owner"].widget = forms.TextInput(
            attrs={"class": "form-control"}
        )

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


class LandInformationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LandInformationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"autocomplete": "off"})

        self.fields["area"].widget = forms.NumberInput(
            attrs={
                "class": "form-control",
                "step": "0.01",
                "min": "0",
            }
        )
        self.fields["square_meter"].widget = forms.NumberInput(
            attrs={
                "class": "form-control",
                "step": "0.01",
                "min": "0",
            }
        )
        self.fields["land_category"].widget = forms.Select(
            attrs={"class": "form-control"},
            choices=[
                ("選択してください", "選択してください"),
                ("宅地", "宅地"),
                ("学校用地", "学校用地"),
                ("公園", "公園"),
                ("境内地", "境内地"),
                ("墓地", "墓地"),
                ("公衆用道路", "公衆用道路"),
                ("鉄道用地", "鉄道用地"),
                ("田", "田"),
                ("畑", "畑"),
                ("牧場", "牧場"),
                ("山林(保安林を除く)", "山林(保安林を除く)"),
                ("保安林", "保安林"),
                ("原野", "原野"),
                ("堤", "堤"),
                ("水道用地", "水道用地"),
                ("運河用地", "運河用地"),
                ("用悪水路", "用悪水路"),
                ("井溝", "井溝"),
                ("ため池", "ため池"),
                ("池沼", "池沼"),
                ("鉱泉地", "鉱泉地"),
                ("塩田", "塩田"),
                ("雑種地", "雑種地"),
            ],
        )
        self.fields["certified_copy_of_land"].widget = forms.Select(
            attrs={"class": "form-control"},
            choices=[
                ("選択してください", "選択してください"),
                ("取得", "取得"),
                ("未取得", "未取得"),
                ("存在なし", "存在なし"),
                ("未調査", "未調査"),
            ],
        )
        self.fields["character_map"].widget = forms.Select(
            attrs={"class": "form-control"},
            choices=[
                ("選択してください", "選択してください"),
                ("取得", "取得"),
                ("未取得", "未取得"),
                ("存在なし", "存在なし"),
                ("未調査", "未調査"),
            ],
        )
        self.fields["survey_map"].widget = forms.Select(
            attrs={"class": "form-control"},
            choices=[
                ("選択してください", "選択してください"),
                ("取得", "取得"),
                ("未取得", "未取得"),
                ("存在なし", "存在なし"),
                ("未調査", "未調査"),
            ],
        )
        self.fields["type_of_rights"].widget = forms.Select(
            attrs={"class": "form-control"},
            choices=[
                ("選択してください", "選択してください"),
                ("所有権", "所有権"),
                ("敷地権", "敷地権"),
                ("地上権", "地上権"),
                ("借地権", "借地権"),
            ],
        )

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


class InfrastructureInformationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InfrastructureInformationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"autocomplete": "off"})

        self.fields["water_supply"].widget = forms.Select(
            attrs={"class": "form-control"},
            choices=[
                ("選択してください", "選択してください"),
                ("公営", "公営"),
                ("井戸水", "井戸水"),
            ],
        )
        self.fields["sweage"].widget = forms.Select(
            attrs={"class": "form-control"},
            choices=[
                ("選択してください", "選択してください"),
                ("公共下水", "公共下水"),
                ("浄化槽", "浄化槽"),
                ("簡易水洗", "簡易水洗"),
                ("その他", "その他"),
            ],
        )
        self.fields["solar_power_generation"].widget = forms.NumberInput(
            attrs={
                "class": "form-control",
                "step": "0.1",
                "max": "10",
                "min": "0",
            }
        )

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
