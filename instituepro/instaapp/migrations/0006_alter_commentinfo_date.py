# Generated by Django 4.1.1 on 2023-05-08 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaapp', '0005_alter_commentinfo_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentinfo',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]