from rest_framework.serializers import ModelSerializer
from grants.models import Grant, Regulation, Organization, Ministry


class GrantSerializer(ModelSerializer):
    class Meta:
        model = Grant


class RegulationSerializer(ModelSerializer):
    class Meta:
        model = Regulation


class OrganizationSerializer(ModelSerializer):
    class Meta:
        model = Organization


class MinistrySerializer(ModelSerializer):
    class Meta:
        model = Ministry
