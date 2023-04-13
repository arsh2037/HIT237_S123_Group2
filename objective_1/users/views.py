from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    return HttpResponse(loader.get_template('index.html').render())

def facts(request):
    return HttpResponse(loader.get_template('facts.html').render())

def data_model(request):
    return HttpResponse(loader.get_template('data_model.html').render())

def reasons(request):
    return HttpResponse(loader.get_template('reasons.html').render())

def benefits(request):
    return HttpResponse(loader.get_template('benefits.html').render())

def solutions(request):
    return HttpResponse(loader.get_template('solutions.html').render())

def resources(request):
    return HttpResponse(loader.get_template('resources.html').render())
def hello(request):
    return render(request, 'calculator_app/index.html')

def calculate(request):
    number_of_people=int(request.GET.get('number_of_people'))
    kilos=int(request.GET.get('kilos'))
    frequency_of_buying=int(request.GET.get('frequency_of_buying'))
    age=int(request.GET.get('age'))
    

    food_Waste= (kilos*frequency_of_buying)/(number_of_people)
    

    params = {'purpose': 'calculated food waste', 'analyzed_text': int(food_Waste)}

    return render(request,'calculator_app/analyze.html',params)