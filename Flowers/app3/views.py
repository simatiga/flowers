from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return render(request, 'test2/test2.html')
    return HttpResponse("Hello, World. You're at the app3 views.")

def page1(request):
    return HttpResponse("Hello, World. You're at the app3 view.........page1.")

def page2(request):
    return HttpResponse("Hello, World. You're at the app3 view.........page2.")

def page3(request):
    return HttpResponse("Hello, World. You're at the app3 view.........page3.")
