# 3. В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
# Нужно перезаписать файл.

# Пример:
#Ангела Меркель 5
#Энакин Скайуокер 5
#Фредди Меркури 3
#Александр Пушкин 4

#Программа выдаст:
#АНГЕЛА МЕРКЕЛЬ 5
#ЭНАКИН СКАЙУОКЕР 5
#Фредди Меркури 3
#Александр Пушкин 4

# P.S. к сожалению с этой задачей не получилось 

import dataclasses
from functions import get_list_data
from typing import List

def elements_to_caps(lst: list, trigger_str: str) -> List[str]:
    for i in range(len(lst)):
        if trigger_str in lst[i]:
            lst[i] = lst[i].upper()
    return lst

lst = get_list_data(
'D:\GeeBr\python\HomeWork\k_08.12.22> get_list_data.txt')

print(elements_to_caps(lst, '5'))

with open('D:\GeeBr\python\HomeWork\k_08.12.22> get_list_data.txt', 'w', encoding='utf-8') as data:
    for i in range(len(lst)):
        dataclasses.writelines(f'{lst[i]}\n')


