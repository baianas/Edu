from os import write
import lxml
import requests
from bs4 import BeautifulSoup as BS
from save_data import write_to_json, write_to_csv

# from save_data import write_to_csv, write_to_json

MAIN_URL = 'https://www.kivano.kg/mobilnye-telefony'
PAGE_COUNT = 5

def open_page(url):
    '''Примнимает адрес страницы, открывает её и возвращает содержимое страницы (html-код)'''
    response = requests.get(url)
    return response.text

def analyze_page_content(page_content):
    '''Принимает код страницы, анализирует его'''
    soup = BS(page_content, 'lxml')
    return soup

def get_product_cards(soup):
    listing = soup.find('div', id = 'w0')
    product_cards = listing.find_all('div', class_='item')
    return product_cards

def get_data_from_card(card):
    image = card.find('img').get('src')

    title = card.find('div', class_='listbox_title').find('a').text

    description = card.find('div', class_='product_text').text.replace(title, '').strip()

    price = card.find('div', class_='listbox_price').find('strong').text

    return {'image': image, 'title': title, 'description': description, 'price': price}

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

    # write_to_json(data)
    write_to_csv(data)

    print(data)
if __name__ == '__main__':
    parse()


# # find() - обращение к одному элементу
# # find_all() - обращение к нескольким однотипным элементам
# # get() - обращение к атрибутам
# # text - обращение к тексту


# #TODO: Сохранить данные в JSON, CSV
# #TODO: использовать user-agent
# #TODO: selenium

# user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
# url = 'https://www.eldorado.ru/c/noutbuki/'

# import requests
# from bs4 import BeautifulSoup as BS
# from selenium import webdriver
# import time

# # response = requests.get(url, headers={'User-Agent': user_agent})
# # print(response.status_code)

# driver = webdriver.Chrome()
# driver.get(url)
# time.sleep(5)

# html = driver.page_source

# soup = BS(html, 'lxml')

# res = soup.find('div', id='listing-container')
# listing = res.find('ul')
# product = listing.find('li', {'data-id': '71557427'})
# price = product.find('span', {'data-pc' : 'offer_price'}).text
# print(price)




# selenium