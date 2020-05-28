from django.shortcuts import render
import requests
import json



def home(request):

	url = "https://covid-193.p.rapidapi.com/statistics"

	querystring = {"country":"Egypt"} #Your country 

	headers = {
	    'x-rapidapi-host': "covid-193.p.rapidapi.com",
	    'x-rapidapi-key': "a86964dd2dmsh9ad362e6a8688bdp1727a1jsn00eb49ebf334" #API Key
	    }

	response = requests.request("GET", url, headers=headers, params=querystring).json()
	
	data = response['response']
	
	d = data[0]


	context = {
		'All':d['cases']['total'],
		'Recovered':d['cases']['recovered'],
		'Deaths':d['deaths']['total'],
		'New':d['cases']['new'],
		'Critical':d['cases']['critical']
	}

	print(d)	
	
	return render(request, 'index.html',context)