from bs4 import BeautifulSoup as BS
import requests
import lxml
import csv

from week4.parsing_project.save_data import write_to_csv

URL = 'https://www.mashina.kg/search/land-rover/all/?currency=2&sort_by=upped_at+desc&time_created=all&page=1'
pages = '&page='

def get_html(url):
    response = requests.get(url)
    return response.text

def get_total_pages(html):
    soup = BS(html, 'lxml')
    pages = soup.find('div', class_ = 'search-results-table')
    last_page = pages.find_all('li')[-1]
    total_pages = last_page.find('a').get('href').split('=')[-1]
    return int(total_pages)

def get_page_data(html):
    soup = BS(html)
    items = soup.find_all('div', class_ = 'list-item')
    cars = []
    
    for car in items:
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
        # write_to_csv(data)
        
    print(data)

def save_file(items, path):
    with open('mashina_kia.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Марка', 'Цена', 'Фотография', 'Краткое описание'])




def main():
    main_url = 'https://www.mashina.kg/search/land-rover/all/?currency=2&sort_by=upped_at+desc&time_created=all&page=1'
    pages = '&page='
    
    total_pages = get_total_pages(get_html(main_url))
    for page in range (1, total_pages + 1):
        url_with_page = main_url + pages + str(page)
        html = get_html(url_with_page)
        # write_to_csv(data)
        get_page_data(html)


main()