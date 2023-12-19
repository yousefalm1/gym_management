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

    gym_class = GymClasses.objects.get(pk=class_id)

    if gym_class.user.count() < gym_class.max_capacity:
        gym_class.user.add(request.user)
        return render(request, 'core/join_success.html',{'class_name': gym_class.class_name})
    else:
        return render(request, 'core/join_failure.html', {'class_name': gym_class.class_name})