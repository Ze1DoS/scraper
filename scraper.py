'''
Сделано в соответствии с курсом:
https://www.youtube.com/watch?v=bC-ZQCE7qEE&list=PLZXVHsCfRw5rX3QklmCwaopTO_bLcSHRt&index=6
'''

import time
import requests
from bs4 import BeautifulSoup as BS

def get_links(url):
    url='https://nextgame.net/catalog/sony-playstation4/' 
    req=requests.get(url)

    bs = BS(req.text, 'html.parser')
    items=bs.find_all('div', {'class':'item_block'})
    links=[]
    for item in items:
            links.append('https://nextgame.net' + item.a['href'])
    return links 

def get_detail(url):
    req=requests.get(url)
    bs = BS(req.text, 'html.parser')
    title = bs.find('h1', {'id':'pagetitle'}).text.strip()
    article = bs.find('div', {'class': 'article'}).find('span', {'class': 'article__value'}).text.strip()
    price = bs.find('span', {'class': 'price_value'}).text.strip()

    print('Название:', title)
    print('Арт.:', article)
    print('Цена:', price)
    print('Ссылка:', url)



url = 'https://nextgame.net/catalog/sony-playstation4/'
for link in get_links(url):
    get_detail(link)
    print('-'*10)
    time.sleep(2)

#ПРЕДЫДУЩИЙ ВАРИАНТ
#Возникли сложности со скрапингом описания, которое находится по другой ссылке, ошибку понял, но решил делать в точности по курсу, во избежание, так сказать

'''
import requests
from bs4 import BeautifulSoup

url = 'https://scrapingclub.com/exercise/list_basic/'
params = {'page': 1}

pages = 2
n = 1

while params['page'] <= pages:
    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

    for n, i in enumerate(items, start=n):
        itemName = i.find('h4', class_='card-title').text.strip()
        itemPrice = i.find('h5').text
        print(f'{n}:  {itemPrice} за {itemName}')

    last_page_num = int(soup.find_all('a', class_='page-link')[-2].text)
    pages = last_page_num if pages < last_page_num else pages
    params['page'] += 1
    '''
