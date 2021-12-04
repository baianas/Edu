from os import write
import lxml
import requests
from bs4 import BeautifulSoup as BS
from save_data import write_to_json, write_to_csv
import csv

MAIN_URL = 'https://www.mashina.kg/search/land-rover/all/?currency=2&sort_by=upped_at+desc&time_created=all&page=1'
PAGE_COUNT = 3

def open_page(url):
    response = requests.get(url)
    return response.text

def analyze_page_content(page_content):
    soup = BS(page_content, 'lxml')
    return soup

def get_product_cards(soup):
    listing = soup.find('div', class_ = 'search-results-table')
    product_cards = listing.find_all('div', class_ = 'list-item')
    return product_cards

def get_data_from_card(card):
        with open('save_hakaton.csv','w') as file:
            columns = ['Название','Цена', 'Картинка','Описание']
            writer = csv.DictWriter(file, columns)
            writer.writeheader()
        try:
            title = card.find('h2', class_='name').text.replace('\n', '').strip()
        except:
            title = ''
        
        try:
            price = card.find('p', class_ = 'price').text.replace('\n', '').strip()

        except:
            price = ''

        try:
            image = card.find('img', class_ = 'lazy-image').get('data-src')
            
        except:
            image = ''

        try:
            description = card.find('div', class_ = 'item-info-wrapper').text.replace('\n', '').strip()
        
        except:
            description = ''

        
        return {'image': image, 'title': title, 'description': description, 'price': price}
        writer.writerow({'Название': title,'Цена':price,'Картинка':image,'Описание':description})

def parse():
    total_product_cards = []
    for page in range(1, PAGE_COUNT + 1):
        page_url = f'{MAIN_URL}?page={page}'
        content = open_page(page_url)
        soup = analyze_page_content(content)
        product_cards = get_product_cards(soup)
        total_product_cards.extend(product_cards)

    data = []
    for card in total_product_cards:
        data.append(get_data_from_card(card))
        
        write_to_csv(data)

parse()

# if __name__ == '__main__':
#     parse()