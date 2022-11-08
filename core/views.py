from django.shortcuts import render
from frontend import *

def moshin1(request):
    return render(request, 'BMW.html')

def moshin2(request):
    return render(request,'equinox.html')

def moshin3(request):
    return render(request,'kaptiva.html')

def moshin4(request):
    return render(request,'malibu.html')
def moshin5(request):
    return render(request,'orlando.html')

def moshin6(request):
    return render(request,'range rower.html')

def gul(request):
    return render(request,'index.html')