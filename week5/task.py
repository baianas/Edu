# with open('test.txt', 'r') as file:
#     text = file.readlines()
#     size = len(text)
#     print(size)

import lxml
import requests
from bs4 import BeautifulSoup as BS
import csv

URL = 'https://vesti.kg/'


source = requests.get(URL).text
soup = BS(source,'lxml')
news1 = soup.find('ul', class_='nspList active nspCol4').text
data = []
data.append(news1)
print(data)

news2 = soup.find('div', class_='itemList').find_all('div', class_= 'itemBody') 
for title in news2:
    a = (title.find('h2').text.replace('\n', '').replace('\t', ''))
# data.extend(a)



# def write_to_csv(data):
#     with open ('vesti.csv', 'w') as file:
#         writer = csv.writer(file)
#         writer.writerow(data)

print(data)        
write_to_csv(data)

