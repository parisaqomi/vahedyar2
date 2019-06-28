from django.shortcuts import render
from .models import Study , Course
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt

def get_index(request):
    if request.method =="GET":
        studies = Study.objects.all()
        return render(request, 'core/index.html', {'studies':studies})

def get_panel(request,study_id):
    if request.method =="GET":
        study = Study.objects.get(pk=study_id)
        request.session['study_id'] = study_id
        return render(request, 'core/panel.html',{'study':study})

def get_courseAssistant(request):
    if request.method =="GET":
        return render(request, 'core/CourseAssistant.html')

def get_courseList(request):
    if request.method =="GET":
        courses = Course.objects.all()
        return render(request, 'core/CourseList.html', {'courses':courses})

def get_courseSituation(request):
    if request.method =="GET":
        return render(request, 'core/CourseSituation.html')

def get_ftForm(request):
    if request.method =="GET":
        return render(request, 'core/first-time-form.html')

def get_login(request):
    if request.method =="GET":
        return render(request, 'core/login.html')

def get_404(request):
    if request.method =="GET":
        return render(request, 'core/404.html')

@csrf_exempt      
def do_login(request):
    redir=''
    if request.method=='GET':
        redir=request.GET.get('next')
        return render(request,'core/login.html')        
    elif request.method=='POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if redir:
                return HttpResponseRedirect(redir)
            return HttpResponseRedirect('/')
        else:
            request.session['error']='کاربری با این مشخصات وجود ندارد'
            return render(request,'core/login.html')

def do_logout(request):
    logout(request)
    return HttpResponseRedirect('login')