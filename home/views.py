from django.shortcuts import render, redirect
from django.template import RequestContext
import requests


def home(request):

    url = 'http://ravigitte.pythonanywhere.com/solve/?exp=integrate(2*x%20+%20y,x)' 
    #params = {'year': year, 'author': author}
    r = requests.get(url)
    data = r.json()
    return render(request, 'home/index.html',{'data':data})


