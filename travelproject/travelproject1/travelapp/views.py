from django.http import HttpResponse
from django.shortcuts import render
from . models import place,team
def demo(request):
    obj=place.objects.all()
    obj2=team.objects.all()
    return render(request,'index.html',{'result':obj,'members':obj2})

# def demo(request):
#     return render(request,'home.html')
# def htm(request):
#     name='demotext'
#     return render(request,'home.html',{'keyy':name})
# def funct(request):
#     return HttpResponse('hi im inmakes')
# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,'result.html',{'result':res})

# Create your views here.
