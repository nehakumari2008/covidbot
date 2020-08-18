import requests


def get_numbers(country):
    url = "https://covid-193.p.rapidapi.com/statistics"

    querystring = {"country": country}

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "6056064999msh0d2f300621f6ac8p1e65f4jsn27e13440f270"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    if len(data['response']) == 1:
        active_cases = data['response'][0]['cases']['active']
        new_cases = data['response'][0]['cases']['new']
        recovered = data['response'][0]['cases']['recovered']
        return active_cases, new_cases, recovered
    else:
        return None


def get_city_wise_data(city):
    url = "https://api.covid19india.org/state_district_wise.json"
    response = requests.get(url)
    data = response.json()
    for key in data:
        state = data[key]
        city = city.title()
        districts = state['districtData']
        if city in districts:
            return districts[city]
    return None


def get_state_wise_data(state):
    url = "https://api.covid19india.org/state_district_wise.json"
    response = requests.get(url)
    data = response.json()
    state = state.title()
    if state in data.keys():
        districtData = data[state]
        districts = districtData["districtData"]

        totalActive = 0
        totalRecovered = 0
        totalConfirmed = 0
        for key in districts:
            district = districts[key]
            totalActive += district["active"]
            totalRecovered += district["recovered"]
            totalConfirmed += district["confirmed"]
        return totalActive, totalConfirmed, totalRecovered

    return None



