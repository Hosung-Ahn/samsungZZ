# Generated by Django 5.1.2 on 2024-10-17 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_collection', '0004_merge_20241017_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubwayAmenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line', models.CharField(max_length=10)),
                ('sttn', models.CharField(max_length=20)),
                ('culture_space', models.CharField(max_length=2)),
                ('wheelchair_lift', models.CharField(max_length=2)),
                ('meeting_place', models.CharField(max_length=2)),
                ('transfer_parking_lot', models.CharField(max_length=2)),
                ('bicycle_storage', models.CharField(max_length=2)),
                ('elevator', models.CharField(max_length=2)),
                ('train_reservation', models.CharField(max_length=2)),
                ('civil_service_machine', models.CharField(max_length=2)),
                ('exchange_kiosk', models.CharField(max_length=2)),
                ('nursing_room', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'subway_amenities',
            },
        ),
        migrations.RenameField(
            model_name='subwaydailytimeslotpassengerdifference',
            old_name='line_number',
            new_name='line',
        ),
        migrations.RenameField(
            model_name='subwaydailytimeslotpassengerdifference',
            old_name='station_name',
            new_name='sttn',
        ),
    ]