# 6.Из списка выше оставьте только те пары, где сумма кортежа кратна 5
# Пример
# [(10,25),(3,4),(4,1)] => [(10,25),(4,1)]

from gbfunctions import random_list
lst_start = random_list(50)
lst_tuple = [i for i in enumerate(lst_start) if i[0] !=[1]]
print(lst_tuple)
lst_div = [i for i in lst_tuple if not (i[0]+i[1]) % 5]
print(lst_div)


