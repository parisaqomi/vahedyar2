from django.shortcuts import render, redirect
from .models import Study, Course, University, Faculty, Score, Chart
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
# import pdb; pdb.set_trace()


def get_index(request):
    if request.method == "GET":
        studies = Study.objects.all()
        charts = Chart.objects.all()
        # breakpoint()
        return render(request, 'core/index.html', {'studies': studies,'charts':charts})
    if request.method == "POST":
        chart_id = request.POST.get('chart')
        chart_id = int(chart_id)
        chart = Chart.objects.get(pk=chart_id)
        student = request.user
        entrance_year=datetime.now().date()
        new_study = Study(chart=chart, student=student,entrance_year=entrance_year)
        new_study.save()
        for course in chart.course.all():
            empty_score = Score(study=new_study, course=course, value=0)
            empty_score.save()
        return redirect('dashboard', study_id=new_study.id)

def get_dashboard(request, study_id):
    if request.method == "GET":
        study = Study.objects.get(pk=study_id)
        # logic for retrieving data about student's status
        total_number_of_courses = len(study.chart.course.all())
        PASSING_SCORE = 10
        passed_scores = study.score_set.filter(value__gte=PASSING_SCORE)
        number_of_passed_courses = len(passed_scores)
        number_of_not_passed_courses = total_number_of_courses - number_of_passed_courses
        sum_passed_units=0
        sum_score_passed=0
        total_units=0
        for item in passed_scores:
            
                sum_unit=item.course.vahed_nazari + item.course.vahed_amali
                sum_passed_units += sum_unit 
                sum_score_passed += sum_unit * item.value 
        if sum_passed_units!=0:
            average=sum_score_passed/sum_passed_units
        else: average=0
        formatted_average = "{:.2f}".format(average)

        for item in study.chart.course.all():
                sum_chart_unit=item.vahed_nazari + item.vahed_amali
                total_units+=sum_chart_unit

        remain_units=total_units-sum_passed_units


        # logic end
        request.session['study_id'] = study_id
        return render(request, 'core/dashboard.html',
                      {'study': study,
                       'passed': number_of_passed_courses,
                       'remaining': number_of_not_passed_courses,
                       'average':formatted_average,
                       'sum_vahed_passed':sum_passed_units,
                       'remain_units':remain_units,
                       'total_units':total_units

                       }
                      )


def get_courseAssistant(request, study_id):
    if request.method == "GET":
        study = Study.objects.get(pk=study_id)
        allcourses = study.chart.course.all().prefetch_related('corequisite_courses').prefetch_related('prerequisite_courses')
        allscore = Score.objects.filter(study_id=study_id)
        PASSING_SCORE = 10
        # list_difference= getDifference(allcourses,allscore)
        allscored_course_ids = allscore.filter(
            value__gte= PASSING_SCORE).values_list('course_id', flat=True)
        allcoursed_id = allcourses.values_list('id', flat=True)
        list_difference = []
        for item in allcoursed_id:
            if item not in allscored_course_ids:
                list_difference.append(item)

        list_allowed_courses = [
            x for x in allcourses if x.id in list_difference]

        study = Study.objects.all()

        return render(request, 'core/CourseAssistant.html', {'study': study, 'list_allowed_courses': list_allowed_courses,'allscored_course_ids':allscored_course_ids,'test':allscore})


def getDifference(x, y):
    symDiff = set(i[0] for i in x) ^ set(i[0] for i in y)
    return [i for i in x if i[0] in symDiff] + [i for i in y if i[0] in symDiff]


def get_courseList(request, study_id):
    if request.method == "GET":
        study = Study.objects.get(pk=study_id)
        request.session['study_id'] = study_id
        courses = Course.objects.all()
        return render(request, 'core/CourseList.html', {
            'courses': courses,
            'study': study
        })


def get_courseSituation(request, study_id):
    if request.method == "GET":
        study = Study.objects.get(pk=study_id)
        # chart = Chart.objects.filter(study = study)
        courses = Course.objects.all()
        # scores = study.score_set.all()
        scores=Score.objects.filter(study_id=study_id)
        request.session['study_id'] = study_id
        return render(request, 'core/CourseSituation.html', {
            'scores': scores,
            'study': study
        })
    if request.method == 'POST':
        pass


def get_study(request):
    if request.method == "GET":
        charts = Chart.objects.all()
        return render(request, 'core/NewStudyForm.html',
                      {'charts': charts})
    if request.method == "POST":
        chart_id = request.POST.get('chart')
        chart_id = int(chart_id)
        chart = Chart.objects.get(pk=chart_id)
        student = request.user
       
        degree =int(chart.degree) 
        new_study = Study(chart=chart, student=student,degree=degree)
        # new_study.degree=degree
        new_study.save()
        for course in chart.course.all():
            empty_score = Score(study=new_study, course=course, value=0)
            empty_score.save()
        return redirect('dashboard', study_id=new_study.id)


def get_login(request):
    if request.method == "GET":
        return render(request, 'core/login.html')


def get_404(request):
    if request.method == "GET":
        return render(request, 'core/404.html')


@csrf_exempt
def do_login(request):
    redir = ''
    if request.method == 'GET':
        redir = request.GET.get('next')
        return render(request, 'core/login.html')
    elif request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if redir:
                return HttpResponseRedirect(redir)
            return HttpResponseRedirect('/')
        else:
            request.session['error'] = 'کاربری با این مشخصات وجود ندارد'
            return render(request, 'core/login.html')


def do_logout(request):
    logout(request)
    return HttpResponseRedirect('login')


@csrf_exempt
def create_or_update_score(request, study_id, course_id):
    if request.method == 'POST':
        study = Study.objects.get(pk=study_id)
        course = Course.objects.get(pk=course_id)
        score_value = request.POST.get('score')
        existing_score = Score.objects.filter(
            study=study).filter(course=course)[0]
        if existing_score:
            existing_score.value = score_value
            existing_score.is_counted = True
            existing_score.save()
            id = existing_score.id
        # else:
        #     score = Score(value=score_value, course=course, study=study,is_counted=True)
        #     score.save()
        #     id = score.id

        result = {'id': id}
        return JsonResponse(result)
