from django.urls import path

from course.views import get_courses

urlpatterns = [
    path('', get_courses),
]