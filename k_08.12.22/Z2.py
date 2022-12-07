# 2. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Не использовать множества.
# Постарайтесь решить за одно условие
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

entered_numbers = list(map(int, input("Введите числа через пробел: ").split()))
print(f"Исходный список: {entered_numbers}")
n_repeating_numbers = []
[n_repeating_numbers.append(i) for i in entered_numbers if i not in n_repeating_numbers]
print(f"Список неповторяющихся элементов исходной последовательности: {n_repeating_numbers}")
