import requests
import lxml
from bs4 import BeautifulSoup as BS

def get_data(url):
    response = requests.get(url).text
    soup = BS(response, 'lxml')
    return soup



def get_info(url):
    soup = get_data(url)
    dep_list = soup.find_all('div', class_ = 'dep-item')
    koko = []
    for dep in dep_list:
        name = dep.find('a', class_ = 'name').text.replace('\n', '')
        fraction = dep.find('div', class_='info').text.replace('\n', '')
        try:
            phone_num = dep.find('a', class_='phone-call').text.replace('\n', '')
        except:
            phone_num = 'Номера нет'
        koko.append((name, fraction, phone_num))
    return koko


info = get_info('http://kenesh.kg/ru/deputy/list/35')
for i in info:
    print(*i)