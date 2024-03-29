from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.urls import reverse

from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import GymClasses, UserProfile, InstructorProfile
from .forms import InstructorProfileForm, GymClassForm, UserProfileForm, UserForm




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
    gym_classes = GymClasses.objects.all()
    users = User.objects.all()
    instructor_profile = InstructorProfile.objects.all()

    return render(request, 'staff_area.html', {'users': users, 'gym_classes':gym_classes, 'instructor_profile':instructor_profile})


def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return render(request, 'delete_user_confirmation.html', {'user': user})


def delete_class(request, class_id):
    gym_class = get_object_or_404(GymClasses, pk=class_id)

    if request.method == 'POST':
        gym_class.delete()
        return redirect('delete_class_confirmation', class_id=class_id)

    return render(request, 'delete_class_confirmation.html', {'gym_class': gym_class})

def delete_class_confirmation(request, class_id):
    return render(request, 'delete_class_confirmation.html', {'class_id': class_id})




# def edit_membership(request, user_id):
#     user = get_object_or_404(User, id=user_id)
#     user_profile = get_object_or_404(UserProfile, user=user)

#     if request.method == 'POST':
#         new_membership_choice = request.POST.get('membership_choice')
#         user_profile.membership_choices = new_membership_choice
#         user_profile.save()

#         # Redirect to the confirmation page
#         return redirect('e', user_id=user.id)

#     return render(request, 'edit_membership.html', {'user_profile': user_profile})

def edit_membership(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user_profile = get_object_or_404(UserProfile, user=user )

    if user.is_staff:
        return HttpResponseForbidden("You cannot edit the admin user's membership.")


    if request.method == 'POST':
        new_membership_choice = request.POST.get('membership_choice')
        user_profile.membership_choices = new_membership_choice
        user_profile.save()

    
        return redirect('edit_membership_confirmation', user_id=user.id)

    return render(request, 'edit_membership.html', {'user_profile': user_profile})


def edit_membership_confirmation(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'edit_membership_confirmation.html', {'user': user})



def user_classes(request, user_id):
    # retrieves a 'User' form the database based on the user_id
    user = get_object_or_404(User, id=user_id)
    # this queries the 'GymClasses' model to get all the instances to use in the template
    gym_classes = GymClasses.objects.filter(users=user )

    # renders the provided html with the context to able to use it in the template
    return render(request, 'classes_joined.html', {'gym_classes': gym_classes})



def add_user_to_class(request, user_id):
    # retrieve the user based on the user_id from the URL
    user = get_object_or_404(User, id=user_id)
    # Retrieve all gym classes from the database
    gym_classes = GymClasses.objects.all()

    # Check if the form is submitted using the POST method
    if request.method == 'POST':
        # get the selected class_id from the submitted form
        class_id = request.POST.get('class_choice')
        # get the gym class based on the selected class_id
        gym_class = get_object_or_404(GymClasses, class_id = class_id)
        # Add the user to the selected gym class
        gym_class.users.add(user)

        return render(request, 'user_added_confirmation.html', {'user': user, 'gym_class': gym_class})



    return render(request, 'add_user_to_class.html', {'user':user, 'gym_classes': gym_classes})





    
def create_instructor_profile(request):
    # checks if the request method is a post request
    if request.method == 'POST':
        # this gathers the data for creating a new instructor profile, the 'request.POST' contains the form data submitted thru the post request and 'request.FILES' contains the uploaded files
        form  = InstructorProfileForm(request.POST, request.FILES)
        if form.is_valid():
            instructor_profile = form.save()
            return render(request, 'create_instructor_confirmation.html', {'instructor_profile': instructor_profile})
    else:
        # if the request is not POST it creates a new InstructorProfileForm to display an empty form to the user.
        form = InstructorProfileForm()

    return render(request, 'create_instructor_profile.html', {'form': form})


def create_instructor_confirmation(request):
    return render(request, 'create_instructor_confirmation.html')


def create_user_profile(request):
    if request.method =='POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user_profile = form.save()
            return render(request, 'create_user_profile_confirmation.html', {'user_profile': user_profile})
    else:
        form = UserProfileForm()

    return render(request, 'create_user_profile.html', {'form': form})





def create_gym_class(request):
    if request.method == 'POST':
        form = GymClassForm(request.POST, request.FILES)
        if form.is_valid():
            gym_class = form.save()
            return render(request, 'create_class_confirmation.html', {'gym_class': gym_class})
    else:
        form = GymClassForm()

    return render(request, 'create_gym_class.html', {'form': form})


def create_class_confirmation(request):
    return render(request, 'create_class_confirmation.html')


def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('edit_user_confirmation')
    else:
        form = UserForm(instance=user)
    
    return render(request, 'edit_user.html', {'form': form, 'user': user})


def edit_user_confirmation(request):
    return render(request, 'edit_user_confirmation.html')


def edit_class(request, class_id):
    gym_class = get_object_or_404(GymClasses, pk=class_id)

    if request.method == 'POST':
        form = GymClassForm(request.POST, request.FILES, instance=gym_class)
        if form.is_valid():
            form.save()
            return redirect('edit_class_confirmation')
    else:
        form = GymClassForm(instance=gym_class)
    
    return render(request, 'edit_class.html', {'form': form, 'gym_class': gym_class})

def edit_class_confirmation(request):
    return render(request, 'edit_class_confirmation.html')




def edit_instructor(request, instructor_id):
    instructor = get_object_or_404(InstructorProfile, pk=instructor_id) 

    if request.method == 'POST':
        form = InstructorProfileForm(request.POST, request.FILES, instance=instructor)
        if form.is_valid():
            form.save()
            return redirect('edit_instructor_confirmation', instructor_id=instructor_id)
    else:
        form = InstructorProfileForm(instance=instructor)

    return render(request, 'edit_instructor.html', {'form': form, 'instructor': instructor})

def edit_instructor_confirmation(request, instructor_id):
    instructor = get_object_or_404(InstructorProfile, pk=instructor_id)
    return render(request, 'edit_instructor_confirmation.html', {'instructor': instructor})


def delete_instructor(request, instructor_id):
    instructor = get_object_or_404(InstructorProfile, pk=instructor_id)

    if request.method == 'POST':
        instructor.delete()
        return redirect("delete_instructor_confirmation", instructor_id=instructor_id)

    return render(request, 'delete_instructor.html', {'instructor': instructor})

def delete_instructor_confirmation(request, instructor_id):
    return render(request, 'delete_instructor_confirmation.html', {'instructor_id': instructor_id})


# def handler404(request, exception):
#     return render(request, 'errors/404.html', status=404)


# def handler500(request):
#     return render(request, "errors/500.html", status=500)