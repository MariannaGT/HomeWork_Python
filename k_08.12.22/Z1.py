# 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

num = int(input("Введите натуральное число: "))
num_1 = 2
roster = []
entered_number = num
while num_1 <= num:
    if num % num_1 == 0:
        roster.append(num_1)
        num //= num_1
        num_1 = 2
    else:
        num_1 += 1
print(f"Простыми множителями числа {entered_number} являются: {roster}")
