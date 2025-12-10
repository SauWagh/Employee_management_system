from django.db import models
import uuid

# Create your models here.
class Employee(models.Model):
    gender_choice =[
        ('G','Gender'),
        ('M','Male'),
        ('F','Female'),
        ('O','Other'),
    ]

    designation_choice = [
        ('YD','Your designation'),
        ('CE','Cloud Engineer'),
        ('DQM','Data Quality Manager'),
        ('DS','Data Science'),
        ('DA','Database Administrator'),
        ('ISS','IT Security Specialist'),
        ('AE','Applications Engineer'),
        ('O','Other'),
    ]

    name = models.CharField(max_length=60)
    mobile_num = models.IntegerField()
    address = models.TextField()
    designation = models.CharField(max_length=20,choices=designation_choice,default='YD')
    employe_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    working = models.BooleanField(default=True)
    gender = models.CharField(max_length=1,choices=gender_choice,default='G')
    email_id = models.EmailField(max_length=100)
    salary = models.FloatField()

    def __str__(self):
        return self.name