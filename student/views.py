from django.shortcuts import render, redirect
from student.models import Student
from django.urls import reverse
from .forms import StudentForm
from django.contrib import messages
# Create your views here.


def student_homepage(request):
    students =Student.objects.all()
    context = {
        'student': students
    }
    return render(request, 'student/INDEX_STU.html', context)


def new_student(request):
    form = StudentForm(request.POST or None, request.FILES or None)
    context = {
        'form': form
    }
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect(('new_student'))
    return render(request, 'student/ADD_STU.html', context)


def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    messages.success(request, 'STUDENT HAS BEEN DELETED')
    return redirect(('student_portal'))


def update_student(request, id):
    instance = Student.objects.get(id=id)
    form = StudentForm(request.POST or None,
                             request.FILES or None, instance=instance)
    context = {
        'form': form
    }
    if form.is_valid():
        form.save()
        messages.success(request, 'STUDENT HAS BEEN UPDATED')
    return render(request, 'student/UPDATE_STU.html', context)

