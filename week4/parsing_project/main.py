import requests
from bs4 import BeautifulSoup
import lxml

def get_html(url):
    response = requests.get(url)
    return response.text
    

get_html('https://www.kivano.kg/noutbuki')
# def main():
#     notebooks_url = 'https://www.kivano.kg/noutbuki'
def get_title(html):
    soup = BeautifulSoup(html, 'lxml')
    # title = soup.find('div', class__='listbox_title')
    list_view = soup.find('div', attrs={'class': 'list-view'})
    list_all = list_view.find_all('div', attrs={'class': 'item product_listbox oh'})
    list_product = list()
    for product in list_all:
        title_product = product.find('div', attrs={'class': 'pull-right'}).find('div', attrs={'class': 'listbox_title'})
        list_product.append(title_product)
    with open('test.txt', 'w') as file:
        for title in list_product:
            file.write(f'{title} \n')
get_title(get_html('https://www.kivano.kg/noutbuki'))