from django.urls import path
from .views import SubwayMonthlyPassengerCounterListView, SubwayDailyPassengerDifferenceView

urlpatterns = [
    path(
        "api/subway-monthly-passenger-list/",
        SubwayMonthlyPassengerCounterListView.as_view(),
        name="subway-monthly-passenger-list",
    ),
    path(
        'api/subway-daily-passenger-difference/<str:date>/<str:line_number>/<str:station_name>/<str:time_slot>/', 
        SubwayDailyPassengerDifferenceView.as_view(),
    ),
]
