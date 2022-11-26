# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Дополнительно: можете проверить, что это действительно число, и что это действительно входит в нужный диапазон
#*Пример:*
#- 6 -> да
#- 7 -> да
#- 1 -> нет

def input_numbers(input_text):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{input_text}"))
            is_OK = True
        except ValueError:
            print("Это не число, попробуйте снова")
    return number
def checkNumber(num):
    if 6 <= num <= 7:
        print("Да, этот день является выходным")
    elif 0 < num < 6:
        print("Нет, это день не является выходным")
    else:
        print("Число не входит в нужный диапазон")

num = input_numbers("Введите число от 1 до 7: ")
checkNumber(num)