from django.urls import path

from course.views import get_courses, create_course, get_course_by_id, delete_course, update_course

urlpatterns = [
    path('', get_courses),
    path('create', create_course),
    path('detail/<int:id>', get_course_by_id),
    path('delete/<int:id>', delete_course),
    path('update/<int:id>', update_course),

]