from django.shortcuts import render
import requests
import json
import random


def index(request):
    countries_and_capitals = requests.get("https://countriesnow.space/api/v0.1/countries/capital")
    result = json.loads(countries_and_capitals.text)

    context = {}
    if result['error']:
        context = {'message': result['msg']}

    countries = []
    countries_with_capital = {}
    for item in result['data']:
        countries.append(item['name'])
        countries_with_capital[item['name']] = item['capital']

    context['country'] = random.choice(countries)

    if 'capital' in request.POST:
        answered_capital = request.POST['capital']
        country = request.POST['country']

        capital = countries_with_capital[country]

        if capital != answered_capital:
            context['message'] = f"The correct capital for {country} is: {capital}. " \
                                 f"Your answer was: {answered_capital}"
        else:
            context['message'] = "Correct answer."

    return render(request, 'quiz/index.html', context)
