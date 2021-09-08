from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
    GENDER_CHOICES = (('M','Male'),('F','Female'),('O','Female'))
    BLOODTYPE = (
			('A+', 'A+ Blood'),
			('B+', 'B+ Blood'),
            ('AB+', 'AB+ Blood'),
            ('O+','O+ Blood'),
            ('A-','A- Blood'),
            ('B-','B- Blood'),
            ('AB-','AB- Blood'),
            ('O-','O- Blood'),
			) 
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200) 
    phone = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length= 50, null= True)
    gender = models.CharField(max_length=1, null=True, choices=GENDER_CHOICES)
    age = models.IntegerField( null=True)
    address = models.CharField(max_length=200)
    blood_group = models.CharField(max_length=3, null=True, choices=BLOODTYPE)
    case_paper = models.CharField(max_length=5, null=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    GENDER_CHOICES = (('M','Male'),('F','Female'),('O','Female'))
    DEPT_CHOICE = (
			('Neurologist', 'Neurologist'),
			('ENT', 'ENT'),
            ('Dentist', 'Dentist'),
            ('Physical Therapy','Physical Therapy'),
            ('Eye Care','Eye Care'),
			) 

    STATUS = (('A','Active'),('I','Inactive'),)
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200) 
    phone = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length= 50, null= True)
    gender = models.CharField(max_length=1, null=True, choices=GENDER_CHOICES)
    age = models.IntegerField(null=True)
    address = models.CharField(max_length=200)
    department = models.CharField(max_length=20, null=True, choices=DEPT_CHOICE)
    salary = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=1, null=True, choices=STATUS)

    def __str__(self):
        return self.name

class Perscription(models.Model):
    
    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
    doctor = models.ForeignKey(Doctor, null=True, on_delete=models.SET_NULL) 
    date = models.DateField(auto_now_add=True, null=True)
    symptoms = models.CharField(max_length=200, null=True)
    perscription = models.CharField(max_length=200, null=True)


    def __str__(self):
        return self.perscription

class Appoinments(models.Model):

    STATUS = (
			('Pending', 'Pending'),
			('Completed', 'completed'),
			)

    patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
    doctor = models.ForeignKey(Doctor, null=True, on_delete=models.SET_NULL) 
    date = models.DateField(null=True)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    status = models.CharField(max_length=15, null=True, choices=STATUS)
    
   

class Account(models.Model):

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, null=True)
    paid = models.IntegerField(default =0, null=True)
    outstanding = models.IntegerField(default =0, null=True)
    Total = models.IntegerField(default =0, null=True)
    