from django.urls import path

from course.views import get_courses, create_course, get_course_by_id

urlpatterns = [
    path('', get_courses),
    path('create/', create_course),
    path('detail/<int:id>/', get_course_by_id),
]