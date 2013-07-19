from rest_framework import generics
from grants.models import Grant, Regulation, Organization, Ministry
from grants.serializers import GrantSerializer, RegulationSerializer
from grants.serializers import OrganizationSerializer, MinistrySerializer


class GrantList(generics.ListAPIView):
    queryset = Grant.objects.all()
    serializer_class = GrantSerializer

    class Meta:
        model = Grant


class RegulationList(generics.ListAPIView):
    queryset = Regulation.objects.all()
    serializer_class = RegulationSerializer

    class Meta:
        model = Regulation


class OrganizationList(generics.ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    class Meta:
        model = Organization


class MinistryList(generics.ListAPIView):
    queryset = Ministry.objects.all()
    serializer_class = MinistrySerializer

    class Meta:
        model = Ministry
