import time
import requests
from bs4 import BeautifulSoup as BS


def get_links_from_page(url):
    url ='https://scrapingclub.com/exercise/list_basic/'
    req = requests.get(url)

    bs_obj = BS(req.text, 'html.parser')

    items = bs_obj.find_all('div', class_='card') 
    links = []
    for item in items:
        links.append(('https://scrapingclub.com' + item.a['href']))
    return links

def get_good_detail(url):
    req = requests.get(url)

    bs_obj = BS(req.text, 'html.parser')
    title = bs_obj.find('h3', class_='card-title').text.strip()
    price = bs_obj.find('div', class_='card-body').find('h4').text.strip()
    text = bs_obj.find('p', class_='card-text').text.strip()
    img = bs_obj.find('img', class_='card-img-top img-fluid')
    print('name: ', title)
    print('price: ', price)
    print('description: ', text)
    print('image: https://scrapingclub.com' + img['src'])

url ='https://scrapingclub.com/exercise/list_basic/'
for link in get_links_from_page(url):
    get_good_detail(link)
    print('-' * 10)
    time.sleep(1)
