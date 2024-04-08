# Generated by Django 5.0.3 on 2024-04-06 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_alter_course_course_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pomodoro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.PositiveSmallIntegerField(choices=[(10, '10 dakika'), (15, '15 dakika'), (20, '20 dakika'), (25, '25 dakika'), (30, '30 dakika'), (35, '35 dakika'), (40, '40 dakika'), (45, '45 dakika'), (50, '50 dakika'), (55, '55 dakika'), (60, '60 dakika'), (65, '65 dakika'), (70, '70 dakika'), (75, '75 dakika'), (80, '80 dakika'), (85, '85 dakika'), (90, '90 dakika'), (95, '95 dakika'), (100, '100 dakika'), (105, '105 dakika'), (110, '110 dakika'), (115, '115 dakika'), (120, '120 dakika')])),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
