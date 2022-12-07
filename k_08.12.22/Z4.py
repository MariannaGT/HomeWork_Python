# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо.
#  При расшифровке происходит обратная операция.
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.


alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
ecryption_step = int(input('Шаг шифровки: '))    # на указанное количество происходит "сдвиг" буквы
message = input("Введите сообщение: ").upper()
result = ''
language = input('Выберите язык RU/EU шифровки: ') 
if language == 'RU':
    for i in message:
        mesto = alfavit_RU.find(i)
        new_mesto = mesto + ecryption_step
        if i in alfavit_RU:
            result += alfavit_RU[new_mesto]
        else:
            result += i
else:
    for i in message:
        mesto = alfavit_EU.find(i)
        new_mesto = mesto + ecryption_step
        if i in alfavit_EU:
            result += alfavit_EU[new_mesto]
        else:
            result += i
print (result)