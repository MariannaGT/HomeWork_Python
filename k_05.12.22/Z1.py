# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: •	[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def sum_indexs(nums):
    s = 0
    for i in range(len(nums)):
        if i % 2 != 0:
            s += nums[i]
    print(f"Сумма равна: {s}")
nums = []
sum_indexs(nums)
nums = list(map(int, input("Введите несколько чисел, через пробел:\n").split()))
sum_indexs(nums)