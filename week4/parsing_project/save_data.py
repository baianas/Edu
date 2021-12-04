import json
import csv
from os import write


def write_to_json(data):
    with open('data.json', 'w', encoding='utf8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

def write_to_csv(data):
    with open ('data_land_rower', 'w') as file:
        columns = ['название', 'цена', 'описание', 'фото']
        writer = csv.DictWriter(file, columns)
        writer.writeheader()
        for prod in data:
            writer.writerow({
                            'название': prod['title'],
                            'описание': prod['description'],
                            'фото': prod['image'],
                            'цена': prod['price'],})

