from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    #return HttpResponse("Hello Candiates welcome to Consultadd")
    my_dict = {'consultadd': "hello I am coming from the index function but getting passed to html code"}
    return render(request, 'consultaddfirstproject/index.html',context=my_dict)


def portfolio(request):
    #return HttpResponse("Hello Candiates welcome to Consultadd")
    return render(request, 'consultaddfirstproject/portfolio.html',context=my_dict)


