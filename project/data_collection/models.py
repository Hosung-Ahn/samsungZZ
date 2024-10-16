from django.db import models


class SubwayMonthlyTimeSlotPassengerCounts(models.Model):
    line = models.CharField(max_length=10)
    sttn = models.CharField(max_length=20)
    hr_4_get_on_nope = models.FloatField()
    hr_4_get_off_nope = models.FloatField()
    hr_5_get_on_nope = models.FloatField()
    hr_5_get_off_nope = models.FloatField()
    hr_6_get_on_nope = models.FloatField()
    hr_6_get_off_nope = models.FloatField()
    hr_7_get_on_nope = models.FloatField()
    hr_7_get_off_nope = models.FloatField()
    hr_8_get_on_nope = models.FloatField()
    hr_8_get_off_nope = models.FloatField()
    hr_9_get_on_nope = models.FloatField()
    hr_9_get_off_nope = models.FloatField()
    hr_10_get_on_nope = models.FloatField()
    hr_10_get_off_nope = models.FloatField()
    hr_11_get_on_nope = models.FloatField()
    hr_11_get_off_nope = models.FloatField()
    hr_12_get_on_nope = models.FloatField()
    hr_12_get_off_nope = models.FloatField()
    hr_13_get_on_nope = models.FloatField()
    hr_13_get_off_nope = models.FloatField()
    hr_14_get_on_nope = models.FloatField()
    hr_14_get_off_nope = models.FloatField()
    hr_15_get_on_nope = models.FloatField()
    hr_15_get_off_nope = models.FloatField()
    hr_16_get_on_nope = models.FloatField()
    hr_16_get_off_nope = models.FloatField()
    hr_17_get_on_nope = models.FloatField()
    hr_17_get_off_nope = models.FloatField()
    hr_18_get_on_nope = models.FloatField()
    hr_18_get_off_nope = models.FloatField()
    hr_19_get_on_nope = models.FloatField()
    hr_19_get_off_nope = models.FloatField()
    hr_20_get_on_nope = models.FloatField()
    hr_20_get_off_nope = models.FloatField()
    hr_21_get_on_nope = models.FloatField()
    hr_21_get_off_nope = models.FloatField()
    hr_22_get_on_nope = models.FloatField()
    hr_22_get_off_nope = models.FloatField()
    hr_23_get_on_nope = models.FloatField()
    hr_23_get_off_nope = models.FloatField()
    hr_0_get_on_nope = models.FloatField()
    hr_0_get_off_nope = models.FloatField()
    hr_1_get_on_nope = models.FloatField()
    hr_1_get_off_nope = models.FloatField()
    hr_2_get_on_nope = models.FloatField()
    hr_2_get_off_nope = models.FloatField()
    hr_3_get_on_nope = models.FloatField()
    hr_3_get_off_nope = models.FloatField()

    class Meta:
        db_table = "subway_monthly_time_slot_passenger_counts"

class SubwayDailyTimeSlotPassengerDifference(models.Model):
    date = models.DateField() 
    line_number = models.CharField(max_length=10)
    station_name = models.CharField(max_length=10)
    time_slot = models.CharField(max_length=20)
    difference = models.IntegerField()
    latitude = models.FloatField(default=37.5665) #latitude, longitude의 null값 방지를 위해
    longitude = models.FloatField(default=126.9780) #임의로 서울시청역 좌표를 디폴트 설정

    class Meta:
        db_table = "subway_daily_time_slot_passenger_difference"