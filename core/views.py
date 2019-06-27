from django.shortcuts import render

def get_index(request):
    if (request.method =="GET"):
        return render(request, 'core/index.html')

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
        return render(request, 'core/CourseList.html')

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
        