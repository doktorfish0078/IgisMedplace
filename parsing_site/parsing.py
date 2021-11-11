import json
from bs4 import BeautifulSoup
import requests


def parse():
    URL = 'https://igis.ru/online'
    html_home_page = requests.get(URL).text

    soup = BeautifulSoup(html_home_page, features='html.parser')

    towns = soup.find_all('div', {'class': 'row-div row-div-sm-2 row-div-md-1 row-div-bg-1'})

    data_towns = {}

    for i in range(0, 28):
        elem_town = towns[i].find('a')
        data_towns[i] = {'town_name': elem_town.text, 'town_href': URL + elem_town['href'], 'hospitals': []}

    for key_town in data_towns:
        html_town_page = requests.get(data_towns[key_town]['town_href']).text
        soup = BeautifulSoup(html_town_page, features='html.parser')
        h3 = soup.find_all('h3')
        h3 = h3[3:]
        for h in h3:
            elem_hospital = h.find('a')
            data_towns[key_town]['hospitals'].append(
                {'name_hospital': elem_hospital.text, 'href_hospital': URL + elem_hospital['href']})
    write_file(data_towns)


def write_file(data):
    with open('dataa.txt', 'w') as outfile:
        json.dump(data, outfile)


def read_file():
    with open('dataa.txt') as json_file:
        data = json.load(json_file)
        for key in data:
            print(data[key])


read_file()
