from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone

from .models import GymClasses, UserProfile, InstructorProfile

def index(request):
    return render(request, 'index.html')


def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if created:
        user_profile.join_date = timezone.now()
        user_profile.save()
    return render(request, 'profile.html', {'user_profile': user_profile})

def instructors(request):
    instructor_profiles = InstructorProfile.objects.all()

    return render(request, 'instructors.html', {'instructor_profiles': instructor_profiles})


def classes(request):
    classes = GymClasses.objects.all()
    return render(request, 'classes.html', {'classes': classes})


def join_class(request, class_id):
# Retrieve the specific gym class from the database based on the provided 'class_id'
    gym_class = get_object_or_404(GymClasses, pk=class_id)



    # Check if the user has a membership
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if user_profile.membership_choices:
    # Checks if the number of users currently registered for the gym class is less than the max capacity if the class is not full the code inside will run
        if gym_class.users.count() < gym_class.max_capacity:
            # Adds the current user to the gym class by updating the 'users' field which is a ManyToManyField
            gym_class.users.add(request.user)
            # After successfully adding the user to the class the view renders the html and passes the class name 
            return render(request, 'join_success.html',{'class_name': gym_class.class_name})
        # If the class is full the code inside the block is executed and renders the join_failure.html template and passes the class name
        else:
            return render(request, 'join_failure.html', {'class_name': gym_class.class_name})
        
    

