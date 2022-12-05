# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
#	[2, 3, 4, 5, 6] => [12, 15, 16];
#	[2, 3, 5, 6] => [12, 15]

def pair_numbers(nums):
    l = len(nums)//2 + 1 if len(nums) % 2 != 0 else len(nums)//2
    new_lst = [nums[i]*nums[len(nums)-i-1] for i in range(l)]
    print(new_lst)
nums = list(map(int, input("Введите несколько чисел, через пробел:\n").split()))
pair_numbers(nums)
