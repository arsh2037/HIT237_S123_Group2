from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'calculator_app/index.html')
# C:\Users\arshh\OneDrive\Desktop\cloned\HIT237_S123_Group2\objective_1\calculatorApp\templates\calculator_app
def calculate(request):
    number_of_people=int(request.GET.get('number_of_people'))
    kilos=int(request.GET.get('kilos'))
    frequency_of_buying=int(request.GET.get('frequency_of_buying'))
    age=int(request.GET.get('age'))
    

    food_Waste= (kilos*frequency_of_buying)/(number_of_people)
    

    params = {'purpose': 'calculated food waste', 'analyzed_text': int(food_Waste)}

    return render(request,'calculator_app/analyze.html',params)