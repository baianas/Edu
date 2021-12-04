"""
Task
Таски

1.Нужно получить статус запроса доступа к странице:

https://stackoverflow.com/questions

присвойте результат запроса к переменной source и выведите эту переменную в консоль.

Примерный вывод в консоли:

200 
"""
# import requests
# url = 'https://stackoverflow.com/questions'
# source = requests.get(url).status_code
# print(source)

"""
2.Спарсите тэги h1, p и ссылку с тэга a из веб-страницы:

http://www.example.com/

и выведите результат в консоль в таком виде:

h1:  Example Domain

p:  This domain is for use in illustrative examples in documents. 
You may use this domain in literature without prior coordination or asking for permission.

a:  https://www.iana.org/domains/example
"""
# import requests
# from bs4 import BeautifulSoup
# import lxml

# url = 'http://www.example.com/'
# source = requests.get(url).text
# soup = BeautifulSoup(source,'lxml')
# s = soup.find('a').get('href')
# print(f"h1: {soup.h1.text}\n")
# print(f"p: {soup.p.text}\n")
# print(f"a: \n{s}")

"""
3.Выведите с главной страницы википедии:

https://www.wikipedia.org/

сколько всего статей есть немецком языке.

Вывод в консоль должен быть таким:

Deutsch

2 590 000+ Artikel 
"""
# import requests
# from bs4 import BeautifulSoup
# import lxml

# url = 'https://www.wikipedia.org/'
# source = requests.get(url).text
# soup = BeautifulSoup(source , 'lxml')
# lang = soup.find('a',id ="js-link-box-de").text
# # inf = soup.find_all('a',id='js-link-box-de').get('small').text
# print(lang)

"""
4.Напишите программу которая проверяет имеет ли страница заголовок(тэг h1) или нет.

Для этого напишите функцию getTitle() которая будет принимать url страницы и возвращать заголовок если он есть, 
если же его нет то будет возвращать "Title could not be found"

 print(getTitle('http://www.example.com/'))
Output:

 <h1>Example Domain</h1>
"""

# import requests
# from bs4 import BeautifulSoup
# import lxml

# def getTitle(url):
#     source = requests.get(url).text
#     soup = BeautifulSoup(source,'lxml')
#     title = soup.find('h1')
#     if title:
#         return title
#     else:
#         return "Title could not be found"


# print(getTitle('http://www.example.com/'))


"""
5.На странице:

https://www.makers.kg

есть названия курсов которые предлагает Makers.

Спарсите названия курсов и выведите в консоль:

Founders  
Coding Bootcamp  
Junior Club  
Studio 
"""
# import requests
# from bs4 import BeautifulSoup
# import lxml

# url ='https://www.makers.kg'
# source = requests.get(url).text
# soup = BeautifulSoup(source,'lxml')
# course = soup.find_all('h3',attrs= {'class':"feature-cards-card-info-title"})
# for i in course:
#     print(i.text)

"""
6.Выведите ссылки на все картинки к каждому из курсов:

Founders

Coding Bootcamp

Junior Club

Studio

В HTML страницы путь к картинке указан неполный:

"./assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a6339fabfdc_95c1a1c.png" 
вам нужно сделать так, чтобы ссылка была выведена в виде:

https://www.makers.kg/assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a6339fabfdc_95c1a1c.png  
при переходе по ссылке, она должна быть рабочей и выводить картинку
"""
# import requests
# url = 'https://www.makers.kg/'

# source = requests.get(url).text

# image1 = url+'assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a6339fabfdc_95c1a1c.png'
# image2 = url+'assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a0abffabfd5_5a615b4.png'
# image3 = url+'assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a54c1fabfd3_1db079d.png'
# image4 = url+'assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a2686fabfd7_79c8646.png'

# print(image1)
# print(image2)
# print(image3)
# print(image4)

""" Этот способ тоже принимает"""

# import requests
# from bs4 import BeautifulSoup

# url = 'https://www.makers.kg/'
# source = requests.get(url).text
# images = ['assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a6339fabfdc_95c1a1c.png',
# 'assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a0abffabfd5_5a615b4.png',
# 'assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a54c1fabfd3_1db079d.png',
# 'assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a2686fabfd7_79c8646.png']
# for image in images:
#     image_new = url + image
#     print(image_new)

"""
7.Теперь спарсите и выведите в консоль описание к каждому курсу.

Например:

Обучаем SMM и digital маркетингу на реальном проекте.  Курс охватывает глубокие знания маркетинга и продаж.
"""

# import requests
# from bs4 import BeautifulSoup
# import lxml

# url ='https://www.makers.kg'
# source = requests.get(url).text
# soup = BeautifulSoup(source,'lxml')
# description = soup.find_all('div', attrs = {'class':'feature-cards-card-info-subtitle'})
# for i in description:
#     print(i.text)


"""
8.Создайте функцию get_info() которая принимает url:

https://www.makers.kg

Функция должна записывать заголовок, описание к курсу и ссылку на картинку в список list_ в виде словаря для каждого курса.

Ключами в словарях должны быть строки 'name','description', 'image_link', а значениями сами заголовки, описания и ссылки на картинки(ссылка также должна быть полной и рабочей).

Выведите данный список в консоль:

print(get_info('https://www.makers.kg')) 
Примерный вывод:

[{'name': 'Founders', 'description': 'Обучаем SMM и digital маркетингу на реальном проекте. Курс охватывает глубокие знания маркетинга и продаж.', 'image_link': 'https://www.makers.kg/assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a6339fabfdc_95c1a1c.png'}, 

{'name': 'Coding Bootcamp', 'description': 'Первый bootcamp по программированию в Кыргызстане. Обучение идет на реальных проектах 5 дней в неделю по 8 часов на протяжении 3 месяцев.', 'image_link': 'https://www.makers.kg/assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a0abffabfd5_5a615b4.png'},

{'name': 'Junior Club', 'description': 'Обучение программированию для продвинутых разработчиков. По окончанию лучшие выпускники могут получить работу в компаниях-партнерах', 'image_link': 'https://www.makers.kg/assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a54c1fabfd3_1db079d.png'}

{'name': 'Studio', 'description': 'Разработка сайтов, приложений и ПО для бизнеса и организаций. Консультация по внедрению IT решений.', 'image_link': 'https://www.makers.kg/assets/5fa63c0bbfbadb648dc12062/5fa63c0c40384a2686fabfd7_79c8646.png'}] 
"""




# import requests
# from bs4 import BeautifulSoup
# import lxml
# def get_info(url): 
#     source = requests.get(url).text 
#     soup = BeautifulSoup(source, "lxml") 
#     info = soup.find("div", class_="feature-cards-wrapper") 
#     cards = info.find_all("div", class_="feature-cards-card-wrapper") 
 
#     list_ = [] 
#     for card in cards: 
#         name = card.find("a").find("h3").text 
#         description = card.find("div", class_="feature-cards-card-info-subtitle").text 
#         image_link = url + card.find("img").get("src")[1:] 
#         dict_ = {"name": name, "description": description, "image_link": image_link} 
#         list_.append(dict_) 
#     return list_ 
         
 
# list_ = get_info("https://www.makers.kg") 
# print(list_)

"""
9.Напишите код который сохраняет все названия категорий со страницы:

https://enter.kg/

в список category_list.

После, напишите функцию которая имеет два параметра - список категорий - categories и ключевое слово - keyword.

Функция должна производить поиск по ключевому слову в списке заголовков category_list и возвращать список  
заголовков которые содержат данное слово (независимо от регистра).

К примеру:

print(find_category(category_list, 'Ноутбуки')) 
Вывод будет:

['Ноутбуки, Ультрабуки, Гот. решения (1281)', 'Ноутбуки (1235)', 'Ноутбуки, Ультрабуки, Гот. решения(1281)', 'Ноутбуки и ультрабуки'] 
"""
# import requests
# from bs4 import BeautifulSoup
# import lxml

# url = 'https://enter.kg/'
# source = requests.get(url).text
# soup = BeautifulSoup(source, 'lxml')

# category_list = soup.find('div',id="wrapper").find('div', id='leftcol')

"""Вот так я могу получить категории"""
# categories = category_list.find_all('ul',attrs ={'class':"VMmenu"})
# for i in categories:
#     print(i.text)

"""Нужно создать функцию, для поиска элементов с ключом keywords, и поместить их в один список"""
# def find_category(category_list):
#     # global category_list
#     categories = category_list.find('ul',class_="VMmenu").get('li')
#     # category_ready = category_list.find(keyword)
#     # return category_ready


# # print(find_category(category_list, 'Ноутбуки')) 