import lxml
import requests
from bs4 import BeautifulSoup as BS

HOST = 'https://www.sulpak.kg'
FILE = 'notebooks.csv'


def get_html(url, params=None):
    response = requests.get(url, verify=False, params=params)
    return response

# def get_pages_count(html):
#     soup = BS(html, 'html.parser')
#     pagination = soup.find_all('span', class_='searchResults')
#     if pagination:
#         return int(pagination[-1].get_text())
#     else:
#         return 1

def get_content(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='searchResults')

    notebooks = []
    for item in items:
        old_price = item.find('div', class_='old-price')
        price = item.find('div', class_='price')
        uah_price = item.find('span', class_='size15')
        if old_price:
            old_price = old_price.get_text().replace(' • ', '')
        else:
            old_price = ''

        print(old_price)
        print(price)
        notebooks.append({
            'title': item.find('div', class_=''),
            'price': item.find('span', class_='hidden'),
            'old_price': old_price
        #     'title': item.find('div', class_='na-card-name').get_text(strip=True),
        #     'link': HOST + item.find('span', class_='link').get('href'),
        #     'usd_price': item.find('strong', class_='green').get_text(),
        #     'uah_price': uah_price,
            
        })
    # return notebooks

# def get_title(html):
#     soup = BS(html, 'lxml')
    


# def main():
#     notebooks_url = 'https://www.sulpak.kg/f/noutbuki'
#     pages = '?page='
#     get_html(notebooks_url)

# main()

get_content('https://www.sulpak.kg/f/noutbuki')
