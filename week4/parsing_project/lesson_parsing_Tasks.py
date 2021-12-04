import requests
import lxml
from bs4 import BeautifulSoup as BS

def get_info(url):
    list_ = []
    source = requests.get(url).text
    soup = BS(source, 'lxml')
    information = soup.find('div', attrs={'class': 'feature-cards-wrapper'})
    inf = information.find_all('div', attrs={'class': 'feature-cards-card-wrapper'})
    for i in inf:
        title = i.find('a').find('h3').text
        description = i.find('div', class_ ='feature-cards-card-info-subtitle').text
        images = i.find('img').get('src')[1:]
        list_.append({'name': title, 'description': description, 'image_link': images})
    return list_
    

print(get_info('https://makers.kg/'))