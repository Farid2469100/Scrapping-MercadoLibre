import requests
from bs4 import BeautifulSoup

string = input('¿Qué quieres buscar? ')
r = requests.get('https://listado.mercadolibre.com.mx/{}#D[A:{}]'.format(string.replace(' ', '-'), string))
contenido = r.content
soup = BeautifulSoup(contenido, 'html.parser')
alldivs = soup.find_all('div', {'class': 'andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16'})
products_array = []

for item in alldivs:
    data = {}
    data['Articulo:'] = item.find('h2', {'class': 'ui-search-item__title'}).text
    data['Precio:'] = item.find('span', {'class': 'andes-money-amount__fraction'}).text
    data['Link:'] = item.find('a', {'class': 'ui-search-item__group__element ui-search-link__title-card ui-search-link'})['href']
    products_array.append(data)
    print(data)