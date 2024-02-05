from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Department(models.Model):
    department = models.CharField(max_length=150, unique=True)
    link = models.URLField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.department
    

class Course(models.Model):
    course = models.CharField(max_length=120)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.course



class Material(models.Model):
    material = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.material
    

class User_profile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    PURPOSE_CHOICES = [
        ('order', 'Place Order'),
        ('enquiry', 'Enquiry'),
        ('return', 'Return'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    age = models.PositiveIntegerField(blank=True) 
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    purpose = models.CharField(max_length=10, choices=PURPOSE_CHOICES)
    materials_provide = models.ManyToManyField(Material)



    def __str__(self):
        return self.name