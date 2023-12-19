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