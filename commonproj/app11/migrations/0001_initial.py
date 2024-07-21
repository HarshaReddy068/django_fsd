# Generated by Django 5.0.6 on 2024-07-21 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=14, unique=True)),
                ('course_name', models.CharField(max_length=70)),
                ('course_credits', models.IntegerField(choices=[(1, 0), (2, 1), (3, 2), (4, 3), (5, 4)])),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_usn', models.CharField(max_length=10, unique=True)),
                ('student_name', models.CharField(max_length=80)),
                ('student_sem', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)])),
                ('enrollment', models.ManyToManyField(to='app11.course')),
            ],
        ),
    ]
