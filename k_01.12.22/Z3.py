# 3. Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым значением.
# Пример:
#  пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0] 


def mint_list(num):
    list_of_numbers = []
    for i in range(num):
        import random
        list_of_numbers.append(random.randint(-50, 30))
    return (list_of_numbers)
def negative_element(element):
    for i in range(len(element)+1):
        if element[i] < 0:
            if i == len(element)-1:
                element.append(0)
            else:
                element.insert(i+1, 0)
    return element
n = input('Введите размер массива: ')
if n.isdigit():
    num = int(n)
    new_list = mint_list(num)
    print(f'Массив случайных чисел:{new_list}')
    try:
        print(f'Массив с добавлением нулевого значения:{negative_element(new_list)}')
    except ImportError:
        print('В массиве нет отрицательных чисел')

