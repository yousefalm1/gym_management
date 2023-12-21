from django.contrib import admin
from django.urls import path,include
from core.views import index, instructors, classes, join_class

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path('instructors/', instructors, name='instructors'),
    path('classes/', classes, name='classes'),
    path('join_class/<int:class_id>/', join_class, name='join_class'),
    path('admin/', admin.site.urls),
    path('', index, name='index'),

]
