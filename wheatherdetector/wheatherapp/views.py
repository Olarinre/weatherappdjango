from django.shortcuts import render
import json
import urllib.request

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city'] # make a request to the api
        req = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=06a10e013b10c18eaa349e1495efb7d7').read()
        #the returned json data from the request made above
        json_data = json.loads(req)
        data ={
            'country_code': str(json_data['sys']),
            'coordinate': str(json_data['coord']['lon']) + '' + str(json_data['coord']['lat']),
            'temp': str(json_data['main']['temp']) + 'k',
            'pressure': str(json_data['main']['pressure']),
            'humidity': str(json_data['main']['humidity']),

        }

    else:
        city =''
        data = {}
    return render(request, 'index.html', {'city': city, 'data':data})