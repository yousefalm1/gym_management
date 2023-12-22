from django.contrib import admin
from django.urls import path,include
from core.views import index, instructors, classes, join_class, profile

urlpatterns = [
    path('instructors/', instructors, name='instructors'),
    path('classes/', classes, name='classes'),
    path('join_class/<int:class_id>/', join_class, name='join_class'),
    path('profile/', profile, name='profile'), 
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('', index, name='index'),

]
