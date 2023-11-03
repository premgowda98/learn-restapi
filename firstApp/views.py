from django.shortcuts import render
from django.http import Http404
from django.urls import reverse
from django.shortcuts import render
# Create your views here.

def root_page(request):
    return render(request, 'firstApp/firstApp.html', {'test': 'from python'})


def loop(request):
    lst = [i for i in range(1,10)]

    #redner always return 200 response code
    return render(request, 'firstApp/loop.html', {
            'list_django': lst
        })

def raise404(request):
    raise Http404() # this automatically renders 404.html in root folder
    




        
