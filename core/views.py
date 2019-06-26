from django.shortcuts import render
from django.http import HttpResponse


def my_view(request):
     return HttpResponse('hello world')
# Create your views here.
def get_index(request):
    if (request.method =="GET"):
        return render(request, 'core/index.html')
def get_t(request):
    if (request.method =="GET"):
        return render(request, 'core/test.html')
def get_panel(request):
    if (request.method =="GET"):
        return render(request, 'core/panel.html')