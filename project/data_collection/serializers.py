from rest_framework import serializers
from .models import (
    SubwayMonthlyTimeSlotPassengerCounts,
    DegreeOfSubwayCongestion,
    SubwayDailyTimeSlotPassengerDifference,
    SubwayAmenities,
    SubwayStationLatLng,
)


class SubwayPassengerCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubwayMonthlyTimeSlotPassengerCounts
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop("id", None)  # id 필드 제거
        return representation


class DegreeOfSubwayCongestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DegreeOfSubwayCongestion
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop("id", None)  # id 필드 제거
        return representation


class SubwayPassengerDifferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubwayDailyTimeSlotPassengerDifference
        fields = ['date', 'line', 'sttn', 'time_slot', 'difference', 'latitude', 'longitude']



class SubwayAmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubwayAmenities
        fields = "__all__"


class SubwayStationLatLngSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubwayStationLatLng
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop("id", None)  # id 필드 제거
        return representation
