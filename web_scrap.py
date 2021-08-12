from bs4 import BeautifulSoup
import requests
#import panda as pd

def request_status_code(url):
    r= requests.get(url)
    return r.status_code 

urls = ['https://listado.mercadolibre.com.co/celulares#D[A:celulares]','https://www.olx.com.co/items/q-celulares']
for url in urls:
    print(request_status_code(url))


url = "https://listado.mercadolibre.com.co/celulares#D[A:celulares]"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

cel = soup.find_all('h2', class_='ui-search-item__title')
cell_phone = list()

for i in cel:
    cell_phone.append(i.text)

print(cell_phone)

price = soup.find_all('span', class_='price-tag')
total_price = list()

for i in price:
    total_price.append(i.text)

print(total_price)
