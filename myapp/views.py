from unittest import result
from django.http import HttpResponse
from django.shortcuts import render
from myapp import ml_model

# Create your views here.

def home(request):
    return render(request, 'index.html',{'title':'Disease Prediction'})

def diabetes(request):    
    if request.method=="POST":
        form_data=request.POST
        result=ml_model.diabetes(form_data)
        data={'title':'Result', 'result':result}
        return render(request, 'result.html', data)
    return render(request, 'diabetes.html', {'title':'Diabetes Prediction'})

def heart(request):
    if request.method=="POST":
        form_data=request.POST
        result=ml_model.heart(form_data)
        data={'title':'Result', 'result':result}
        return render(request, 'result.html', data)
    return render(request, 'heart.html', {'title':'Heart Prediction'})

def liver(request):
    if request.method=="POST":
        form_data=request.POST
        result=ml_model.liver(form_data)
        data={'title':'Result', 'result':result}
        return render(request, 'result.html', data)
    return render(request, 'liver.html', {'title':'Liver Prediction'})