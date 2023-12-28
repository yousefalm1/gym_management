from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path,include
from core.views import index, instructors, classes, join_class, profile, cancel_class, staff_area


urlpatterns = [
    path('instructors/', instructors, name='instructors'),
    path('classes/', classes, name='classes'),
    path('join_class/<int:class_id>/', join_class, name='join_class'),
    path('cancel_class/<int:class_id>/', cancel_class, name='cancel_class'),
    path('profile/', profile, name='profile'), 
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('staff/',staff_area, name='staff_area' ),
    path('', index, name='index'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
