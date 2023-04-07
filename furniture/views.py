from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'furniture/index.html')

def sahad(request):
    return render(request,'furniture/livingroom.html')

def fahim(request):
    return render(request,'furniture/bedroom.html')

def rasu(request):
    return render(request,'furniture/dining.html')

def shabeer(request):
    return render(request,'furniture/studyroom.html')

def shameer(request):
    return render(request,'furniture/store.html')

def musthafa(request):
    return render(request,'furniture/kitchen.html')