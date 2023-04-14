from django.urls import path
from . import views
from users.views import Info
urlpatterns = [
    path('', views.index, name='index'),
    path('facts', views.facts, name='facts'),
    path('data_model', views.data_model, name='data_model'),
    path('reasons', views.reasons, name='reasons'),
    path('benefits', views.benefits, name='benefits'),
    path('solutions', views.solutions, name='solutions'),
    path('resources', views.resources, name='resources'),
    path('calculator', views.Calindex, name='calculator'),
    path('analyze', views.calculate, name='calculated'),
    path('info',  views.wastage, name='info'),
    
]
