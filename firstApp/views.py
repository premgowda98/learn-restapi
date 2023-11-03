from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
# Create your views here.

def root_page(request):
    return render(request, 'firstApp/firstApp.html', {'test': 'from python'})


def loop(request):
    lst = [i for i in range(1,10)]
    
    return render(request, 'firstApp/loop.html', {
            'list_django': lst
        })




        
