import requests
import lxml
from bs4 import BeautifulSoup
import csv
from save_data import write_to_csv

def get_html(url):
    response = requests.get(url)
    return response.text
    
def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('div', class_ = 'search-results-table')
    last_page = pages.find_all('li')[-1]
    total_pages = last_page.find('a').get('href').split('=')[-1]
    return int(total_pages)

def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Марка', 'Ссылка', 'Цена в $', 'Цена в UAH', 'Город'])
        for item in items:
            writer.writerow([item['Марка'], item['Цена'], item['Фотография'], item['Описание']])

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    product_list = soup.find('div', class_ = 'table-view-list')
    products = product_list.find_all('div', class_ = 'list-item')
    for car in products:
        
        try:
            title = car.find('h2', class_='name').text.replace('\n', '').strip()
        except:
            title = ''
        
        try:
            price = car.find('p', class_ = 'price').text.replace('\n', '').strip()

        except:
            price = ''

        try:
            image = car.find('img', class_ = 'lazy-image').get('data-src')
            
        except:
            image = ''

        try:
            description = car.find('div', class_ = 'item-info-wrapper').text.replace('\n', '').strip()
            print(description)
        except:
            description = ''

        
        data = {'Марка': title, 'Цена': price, 'Фотография': image, 'Опсиание': description}

        

def parse():
    main_url = 'https://www.mashina.kg/search/land-rover/all/?currency=2&sort_by=upped_at+desc&time_created=all&page='
    pages = '&page='

    total_pages = get_total_pages(get_html(main_url))
    for page in range (1, total_pages + 1):
        url_with_page = main_url + pages + str(page)
        html = get_html(url_with_page)
        get_page_data(html)
        write_to_csv(get_page_data(html))
   

parse()

