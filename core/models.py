from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

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
    membership_choices = models.CharField(max_length=50)
    join_date = models.DateField()
    new_membership_purchase = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class InstructorProfile(models.Model):
    instructor = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=50)
    certification = models.TextField()

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
    max_capacity = models.IntegerField()
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.class_name