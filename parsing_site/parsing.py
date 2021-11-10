from bs4 import BeautifulSoup
import requests

URL = 'https://igis.ru/online'
html_home_page = requests.get(URL).text

soup = BeautifulSoup(html_home_page, features='html.parser')

towns = soup.find_all('div', {'class': 'row-div row-div-sm-2 row-div-md-1 row-div-bg-1'})

towns_link = []

for i in range(0, 28):
    towns_link.append(towns[i].find('a')['href'])

hospitals = []

for town_link in towns_link:
    html_town_page = requests.get(URL + town_link).text
    soup = BeautifulSoup(html_town_page, features='html.parser')
    h3 = soup.find_all('h3')
    h3 = h3[3:]
    for h in h3:
        hospitals.append(h.find('a')['href'])
