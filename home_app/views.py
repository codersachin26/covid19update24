from django.shortcuts import render
import requests


# Create your views here.


def home(request):
    endpoint = 'https://api.covid19api.com/summary'
    response = requests.get(endpoint)
    data = response.json

    for country in  data()['Countries']:
        if country['CountryCode'] == 'IN':
            india = country
            break
        else:
            continue

    
    return render(request,'index.html',{'data':data,'india':india})
