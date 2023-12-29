from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse

from django.utils import timezone
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
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
    else:
        return render(request, 'no_membership.html' )
    

def cancel_class(request, class_id):
    gym_class = get_object_or_404(GymClasses, pk=class_id)

    if request.user in gym_class.users.all():
        gym_class.users.remove(request.user)
        return render(request, 'cancel_success.html', {'class_name': gym_class.class_name})


def staff_area(request):

    users = User.objects.all()
    return render(request, 'staff_area.html', {'users': users})


def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('staff_area')

@login_required
def edit_membership(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user_profile = get_object_or_404(UserProfile, user=user )

    if request.method == 'POST':
        new_membership_choice = request.POST.get('membership_choice')
        user_profile.membership_choices = new_membership_choice
        user_profile.save()

    return render(request, 'edit_membership.html', {'user_profile': user_profile})


def user_classes(request, user_id):
    # retrieves a 'User' form the database based on the user_id
    user = get_object_or_404(User, id=user_id)
    # this queries the 'GymClasses' model to get all the instances to use in the template
    gym_classes = GymClasses.objects.filter(users=user )

    # renders the provided html with the context to able to use it in the template
    return render(request, 'classes_joined.html', {'gym_classes': gym_classes})



def add_user_to_class(request, user_id):
    user = get_object_or_404(User, id=user_id)
    gym_classes = gym_classes.object.all()

    if request.method == 'POST':
        class_id = request.POST.get('class_choice')
        gym_class = get_object_or_404(GymClasses, class_id = class_id)
        gym_class.users.add(user)

        return redirect('staff_area')

    return render(request, 'add_user_to_Class.html', {'user':user, 'gym_class': gym_class})