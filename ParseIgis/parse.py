from bs4 import BeautifulSoup
import requests

URL = 'https://igis.ru/online'
html_home_page = requests.get(URL).text
soup = BeautifulSoup(html_home_page, features="html.parser")

towns = soup.find_next('div', {'class', 'row-div'})
print(towns)
# for town in towns:
#     print(town.find('a').text)
