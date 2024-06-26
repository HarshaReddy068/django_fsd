# Generated by Django 5.0.6 on 2024-06-12 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('course_code', models.CharField(max_length=14)),
                ('course_name', models.CharField(max_length=70)),
                ('course_credits', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('student_usn', models.CharField(max_length=10)),
                ('student_name', models.CharField(max_length=80)),
                ('student_sem', models.IntegerField()),
                ('enrolment', models.ManyToManyField(to='app5.course')),
            ],
        ),
    ]