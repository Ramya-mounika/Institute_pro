# Generated by Django 4.1.1 on 2023-05-08 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaapp', '0008_alter_commentinfo_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentinfo',
            name='rating',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='commentinfo',
            name='user_name',
            field=models.CharField(max_length=50),
        ),
    ]
