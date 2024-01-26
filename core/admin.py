from django.contrib import admin
from .models import UserProfile, InstructorProfile, MembershipType, GymClasses

# Register your models here
admin.site.register(UserProfile)
admin.site.register(InstructorProfile)
admin.site.register(MembershipType)
admin.site.register(GymClasses)
