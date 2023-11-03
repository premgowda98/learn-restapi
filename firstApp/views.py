from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
# Create your views here.

def index(Request):
    return HttpResponse("Hi")

def index2(Request):
    return HttpResponse("Hi2")

def _handle_all(request, app):
    text = None

    if app=='app1':
        text = "Hi1"
    elif app=='app2':
        text="Hi2"
    else:
        return HttpResponseNotFound()
    
    return HttpResponse(text)

apps = {
    'app1': 'Hi1',
    'app2': 'Hi2'
}

def handle_all_int(request, app):
    apps_key = list(apps.keys())
    try:
        apps_name = apps_key[app]

        #apps-num is the name of the url specifiyed in django apps urls.py file
        redirect_path = reverse('apps-num', args=[apps_name])

        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound()


def handle_all(request, app):
    if app in apps.keys():
        return HttpResponse(apps[app])
    else:
        return HttpResponseNotFound()
    

def root_page(request):
    return render(request, 'firstApp/firstApp.html', {'test': 'from python'})


        
