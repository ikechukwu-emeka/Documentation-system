from django.urls import path
from .views import *

urlpatterns = [
    path('student', student_homepage, name = 'student_portal'),
    path('new-student', new_student, name = 'new_student'),
    path('deleted/<int:id>/', delete_student,
    name = 'delete_student'),
    path('updated/<int:id>/', update_student,
   name = 'update_student'),
]
