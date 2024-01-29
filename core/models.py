
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class MembershipType(models.Model):
    membership_type_id = models.AutoField(primary_key=True)
    membership_type_name = models.CharField(max_length=100)

    def __str__(self):
        return self.membership_type_name

class UserProfile(models.Model):

    MEMBERSHIP_CHOICES = [
        ('bronze', 'Bronze'),
        ('silver', 'Silver'),
        ('gold', 'Gold'),
        ('None', 'None'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership_choices = models.CharField(choices=MEMBERSHIP_CHOICES,default='None')
    join_date = models.DateField(default=timezone.now)
    new_membership_purchase = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class InstructorProfile(models.Model):
    instructor = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=50)
    certification = models.TextField()
    display_name = models.CharField(max_length=100, default='Default Display Name')
    instructor_image = models.ImageField(upload_to='images/',null=True, blank=True)

    def __str__(self):
        return self.instructor.username


class GymClasses(models.Model):
    
    class_id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=100)
    room_number = models.CharField(max_length=50)
    description = models.TextField(default="Your default description goes here")
    max_capacity = models.IntegerField()
    users = models.ManyToManyField(User)
    class_image = models.ImageField(upload_to='images/', null=True, blank=True)
    instructors = models.ManyToManyField(InstructorProfile)

    def __str__(self):
        return self.class_name
    

