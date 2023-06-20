from django.db import models


class contactData(models.Model):
    firstName=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=100)
    gender=models.CharField(max_length=50)
    course=models.CharField(max_length=50)

class Courses(models.Model):
    courseName=models.CharField(max_length=50)
    fee=models.IntegerField()
    duration=models.CharField(max_length=50)
    startDate=models.DateTimeField(max_length=100)
    trainerName=models.CharField(max_length=50)
    trainerExp=models.CharField(max_length=50)
    trainerMode=models.CharField(max_length=50)


class CommentInfo(models.Model):
    user_name=models.CharField(max_length=50)
    rating=models.IntegerField(default=10)
    content=models.TextField(max_length=75)
    date=models.DateTimeField(auto_now_add=True)
