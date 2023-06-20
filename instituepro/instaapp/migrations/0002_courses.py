# Generated by Django 4.1.1 on 2023-05-05 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=50)),
                ('fee', models.IntegerField()),
                ('duration', models.CharField(max_length=50)),
                ('startDate', models.DateTimeField(max_length=100)),
                ('trainerName', models.CharField(max_length=50)),
                ('trainerExp', models.CharField(max_length=50)),
                ('trainerMode', models.CharField(max_length=50)),
            ],
        ),
    ]
