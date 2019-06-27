from django.shortcuts import render
from .models import Study , Course


def get_index(request):
    if (request.method =="GET"):
        studies = Study.objects.all()
        return render(request, 'core/index.html', {'studies':studies})


def get_t(request):
    if (request.method =="GET"):
        return render(request, 'core/test.html')

def get_panel(request):
    if (request.method =="GET"):
        return render(request, 'core/panel.html')

def get_courseAssistant(request):
    if (request.method =="GET"):
        return render(request, 'core/CourseAssistant.html')

def get_courseList(request):
    if (request.method =="GET"):
        courses = Course.objects.all()
        return render(request, 'core/CourseList.html', {'courses':courses})

def get_courseSituation(request):
    if (request.method =="GET"):
        return render(request, 'core/CourseSituation.html')

def get_ftForm(request):
    if (request.method =="GET"):
        return render(request, 'core/first-time-form.html')

def get_login(request):
    if (request.method =="GET"):
        return render(request, 'core/login.html')

def get_404(request):
    if (request.method =="GET"):
        return render(request, 'core/404.html')
        