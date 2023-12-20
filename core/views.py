from django.shortcuts import render
from django.http import HttpResponse
from .models import GymClasses

def index(request):
    return render(request, 'core/index.html')


def instructors(request):
    return render(request, 'core/instructors.html')


def classes(request):
    classes = GymClasses.objects.all()
    return render(request, 'core/classes.html', {'classes': classes})


def join_class(request, class_id):
# Retrieve the specific gym class from the database based on the provided 'class_id'
    gym_class = GymClasses.objects.get(pk=class_id)

# Checks if the number of users currently registered for the gym class is less than the max capacity if the class is not full the code inside will run
    if gym_class.user.count() < gym_class.max_capacity:
        # Adds the current user to the gym class by updating the 'users' field which is a ManyToManyField
        gym_class.user.add(request.user)
        # After successfully adding the user to the class the view renders the html and passes the class name 
        return render(request, 'core/join_success.html',{'class_name': gym_class.class_name})
    # If the class is full the code inside the block is executed and renders the join_failure.html template and passes the class name
    else:
        return render(request, 'core/join_failure.html', {'class_name': gym_class.class_name})