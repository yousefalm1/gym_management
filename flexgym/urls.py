from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path,include
from core.views import index, instructors, classes, join_class, profile, cancel_class, staff_area, delete_user, edit_membership, user_classes, add_user_to_class, create_instructor_profile, create_gym_class, edit_class, delete_class, edit_instructor, delete_instructor,create_instructor_confirmation, create_class_confirmation, create_user_profile, edit_user,edit_user_confirmation, delete_class_confirmation, delete_instructor_confirmation


urlpatterns = [
    path('instructors/', instructors, name='instructors'),
    path('classes/', classes, name='classes'),
    path('join_class/<int:class_id>/', join_class, name='join_class'),
    path('cancel_class/<int:class_id>/', cancel_class, name='cancel_class'),
    path('profile/', profile, name='profile'), 
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('staff/',staff_area, name='staff_area' ),
    path('delete_user/<int:user_id>/', delete_user, name='delete_user'),

    path('edit_user/<int:user_id>/', edit_user, name='edit_user'),
    path("edit_user_confirmation/", edit_user_confirmation, name="edit_user_confirmation"),



    path('edit_membership/<int:user_id>/', edit_membership, name='edit_membership'),


    path('user_classes/<int:user_id>/', user_classes, name='user_classes'),
    path('add_user_to_class/<int:user_id>/', add_user_to_class, name="add_user_to_class"),

    path('create_instructor_profile/', create_instructor_profile, name='create_instructor_profile'),

    path('create_gym_class/', create_gym_class, name='create_gym_class'),
    path("create_class_confirmation/", create_class_confirmation , name="create_class_confirmation"),

    path('edit_class/<int:class_id>/', edit_class, name ='edit_class'),
    path('delete_class/<int:class_id>/', delete_class, name = 'delete_class'),
    path('delete_class_confirmation/<int:class_id>/', delete_class_confirmation, name='delete_class_confirmation'),



    path('edit_instructor/<int:instructor_id>/',edit_instructor , name='edit_instructor'),
    path('delete_instructor/<int:instructor_id>/', delete_instructor, name= 'delete_instructor'),
    path('delete_instructor_confirmation/<int:instructor_id>/', delete_instructor_confirmation, name='delete_instructor_confirmation'),

    path('create_user_profile/', create_user_profile, name='create_user_profile'),


    path('', index, name='index'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
