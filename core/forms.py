from django import forms
from .models import InstructorProfile, GymClasses, UserProfile

class InstructorProfileForm(forms.ModelForm):
    #  provide metadata about the form so for this case it is about the model InstructorProfile so the form will be based off the fields in the model
     class Meta:
        model = InstructorProfile
        # this specifies what fields for the model should be in the form 
        fields = ['instructor','specialization', 'certification', 'display_name', 'instructor_image']


class GymClassForm(forms.ModelForm):
    class Meta:
        model = GymClasses
        fields = ['class_name', 'room_number', 'description', 'max_capacity', 'class_image', 'instructors']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user', 'membership_choices', 'join_date', 'new_membership_purchase']