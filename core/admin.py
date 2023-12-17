from django.contrib import admin
from .models import UserProfile, InstructorProfile, MemberProfile, AdminProfile, MembershipType, GymClasses

# Register your models here
admin.site.register(UserProfile)
admin.site.register(InstructorProfile)
admin.site.register(MemberProfile)
admin.site.register(AdminProfile)
admin.site.register(MembershipType)
admin.site.register(GymClasses)
