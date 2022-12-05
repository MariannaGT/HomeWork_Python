# 5.Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи


num = int(input("Введите число:\n"))
fibonacci_1 = [0, 1]
fibonacci_2 = []
fibonacci_3 = []
for i in range(2, num+1):
    fibonacci_1.append(fibonacci_1[i-2]+fibonacci_1[i-1])
for i in range(1, len(fibonacci_1)):
    fibonacci_2.append(-fibonacci_1[i])
fibonacci_1.reverse()
fibonacci_3 = fibonacci_2 + fibonacci_1
print("Cписок чисел:\n ",fibonacci_3)