
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
    ]


    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership_choices = models.CharField(choices=MEMBERSHIP_CHOICES)
    join_date = models.DateField(default=timezone.now)
    new_membership_purchase = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class InstructorProfile(models.Model):
    instructor = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=50)
    certification = models.TextField()
    display_name = models.CharField(max_length=100, default='Default Display Name')
    instructor_image = models.ImageField(upload_to='instructors_photo', null=True, blank=True)




    def __str__(self):
        return self.instructor.username


class MemberProfile(models.Model):
    member = models.OneToOneField(User, on_delete=models.CASCADE)
    membership_type = models.ForeignKey(MembershipType, on_delete=models.CASCADE, null=True) 
    renewal_date = models.DateField()

    def __str__(self):
        return self.member.username


class AdminProfile(models.Model):
    admin = models.OneToOneField(User, on_delete=models.CASCADE)
    is_superadmin = models.BooleanField(default=False)

    ROLE_CHOICES = [
        ('admin', 'Administrator'),
        ('staff', 'Staff')
        
    ]

    roles = models.CharField(max_length=100, choices=ROLE_CHOICES)

    def __str__(self):
        return self.admin.username



class GymClasses(models.Model):
    
    class_id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=100)
    room_number = models.CharField(max_length=50)
    description = models.TextField(default="Your default description goes here")
    max_capacity = models.IntegerField()
    users = models.ManyToManyField(User)
    class_image = models.ImageField(upload_to='class_images', null=True, blank=True)

    def __str__(self):
        return self.class_name