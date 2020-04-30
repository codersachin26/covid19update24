from django.shortcuts import render
import requests
import json

# Create your views here.


def home(request):
    endpoint = 'https://api.covid19api.com/summary'
    response = requests.get(endpoint)
    data = response.json
    india = data()['Countries'][101]
    return render(request,'index.html')