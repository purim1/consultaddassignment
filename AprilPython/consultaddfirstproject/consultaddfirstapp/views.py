from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    #return HttpResponse("Hello Candiates welcome to Consultadd")
    return render(request, 'consultaddfirstproject/index.html')