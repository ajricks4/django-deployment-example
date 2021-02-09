from django.shortcuts import render

# Create your views here.

def index(request):
    context={
        'text':'hello world',
        'number':100
    }
    return render(request, 'basicapp/index.html',context)

def other(request):
    context={}
    return render(request, 'basicapp/other.html',context)

def relative(request):
    context={}
    return render(request, 'basicapp/relative_url_template.html',context)