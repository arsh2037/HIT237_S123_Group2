from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic import TemplateView



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
def Calindex(request):
    return render(request, 'calculator_app/index.html')
def calculate(request):
    number_of_people=int(request.GET.get('number_of_people'))
    kilos=int(request.GET.get('kilos'))
    frequency_of_buying=int(request.GET.get('frequency_of_buying'))
    age=int(request.GET.get('age'))
    

    food_Waste= (kilos*frequency_of_buying)/(number_of_people)
    

    params = {'purpose': 'calculated food waste', 'analyzed_text': int(food_Waste)}

    return render(request,'calculator_app/analyze.html',params)

def wastage(request):
    context={
        'cities':create_wastage()
    }
    return render(request,'Impact/info.html',context)
def create_wastage():
    Waste=[]
    Waste.append(str(Info("Perth",3000,"2000 People")))
    Waste.append(str(Info("Melbourne",54000,"100000 People")))
    Waste.append(str(Info("Sydney",58000,"120000 People")))
    Waste.append(str(Info("Darwin",2322,"1200 People")))
    
    return Waste
    
class Info:
    def __init__(self,city,wastage,impact):
        self.city = city
        self.wastage = wastage
        self.impact =impact
    def __str__(self):

        return str(self.city) + ", " + str(self.wastage) + ", " + str(self.impact)