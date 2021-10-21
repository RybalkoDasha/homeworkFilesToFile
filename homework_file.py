import os
from pprint import pprint

file_path = os.path.join(os.getcwd(), 'file1.txt')


with open(file_path, encoding="utf-8") as file:
    cook_book = {}
    for recipe in file:
        cook_book[recipe.strip()] = []
        counter = int(file.readline().strip())
        for item in range(counter):
            ingredient_name, quantity, measure = file.readline().split('|')
            cook_book[recipe.strip()].append(
                {'ingredient_name': ingredient_name.strip(), 'quantity': int(quantity.strip()),
                 'measure': measure.strip()}
            )
        file.readline()
    # pprint(cook_book)

def get_shop_list_by_dishes(dishes_list, person_count):
    ingridient = {}
    for dishes in dishes_list:
        for key, value in cook_book.items():
            if dishes == key:
                for element in value:
                    if element['ingredient_name'] not in ingridient:
                        ingridient[element['ingredient_name']] = {'measure': element['measure'],
                                                                  'quantity': element['quantity'] * person_count}
                    else:
                        ingridient[element['ingredient_name']]['quantity'] += element['quantity'] * person_count

    pprint(f"{ingridient}")









