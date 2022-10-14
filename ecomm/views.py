from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'pages/index.html')

def slider(request):
    return render(request,'slider.html')