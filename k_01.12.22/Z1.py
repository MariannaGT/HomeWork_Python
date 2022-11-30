# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. 
# Учтите, что числа могут быть отрицательными
# Пример:
#	67.82 -> 23
#	(-0.56) -> 11

def input_numbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = float(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number

def sum_nums(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum

num = input_numbers("Введите число: ")

print(f"Сумма цифр = {sum_nums(num)}")