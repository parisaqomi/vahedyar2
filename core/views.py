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