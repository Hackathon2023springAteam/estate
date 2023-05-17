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

        self.fields["control_number"].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields["property_name"].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields["location"].widget = forms.TextInput(attrs={'class': 'form-control'})
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


class CityPlanningForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CityPlanningForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"autocomplete": "off"})
        
        self.fields["zoning"].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields["public_land_expansion_act"].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields["road_width"].widget = forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'})
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


class BuildingInformationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BuildingInformationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"autocomplete": "off"})

        self.fields["certified_copy_of_building"].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields["building_drawing"].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields["building_confirmation_screen"].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields["property_tax_assessment_certificate"].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields["building_use"].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields["type_of_rights"].widget = forms.TextInput(attrs={'class': 'form-control'})
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


class LandInformationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(LandInformationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"autocomplete": "off"})
        
        self.fields["area"].widget = forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'})
        self.fields["square_meter"].widget = forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'})
        self.fields["land_category"].widget = forms.NumberInput(attrs={'class': 'form-control', 'step': '1'})
        self.fields["certified_copy_of_land"].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields["character_map"].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields["survey_map"].widget = forms.TextInput(attrs={'class': 'form-control'})
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


class InfrastructureInformationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InfrastructureInformationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"autocomplete": "off"})

        self.fields["water_supply"].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields["sweage"].widget = forms.TextInput(attrs={'class': 'form-control'})
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
