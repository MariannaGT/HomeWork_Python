# 4. Дан список случайных чисел. Оставьте только те, сумма цифр которых четна

import random
random_numbers = []
sum_numbers = 0
random_numbers = [random.randint(1,10) for i in range(1,10)] 
print(f"Cписок случайных чисел: {random_numbers}")

for i in random_numbers: 
    if (i%2) == 0:
        sum_numbers += i
print(f"Сумма четных чисел из списка: {sum_numbers}")