import time
import requests
from bs4 import BeautifulSoup as BS

def get_links_from_page(url):
    url='https://nextgame.net/catalog/sony-playstation4/' 
    req=requests.get(url)

    bs_obj = BS(req.text, 'html.parser')
    items=bs_obj.find_all('div', class_='item_block')
    links=[]
    for item in items:
            links.append('https://nextgame.net' + item.a['href'])
    return links 


# url='https://nextgame.net/catalog/sony-playstation4/'    

# all_goods = [] 
# page_url = f'{url}?PAGEN_1={1}'
# new_goods = get_links_from_page(page_url)
# all_goods.extend(new_goods)
# print(*all_goods, sep='\n')

def get_good_detail(url):
    req=requests.get(url)
    bs_obj = BS(req.text, 'html.parser')
    title = bs_obj.find('h1', {'id':'pagetitle'}).text.strip()
    article = bs_obj.find('div', {'class': 'article'}).find('span', {'class': 'article__value'}).text.strip()
    price = bs_obj.find('span', {'class': 'price_value'}).text.strip()

    print('Название:', title)
    print('Артикул:', article)
    print('Цена:', price)
    print('Ссылка:', url)



url = 'https://nextgame.net/catalog/sony-playstation4/'
for link in get_links_from_page(url):
    get_good_detail(link)
    print('-'*10)
    time.sleep(5)