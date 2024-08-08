from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'meio_ambiente.html')
   

def plantio(request):
    return HttpResponse("Plantando")

