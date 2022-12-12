# 4. Создайте два списка — один с названиями языков программирования, другой — с их нумерацией.
# ['python', 'c#']
# [1,2]


languages = ['Python', 'C#', 'Java', 'C++', 'PHP']
numbers = [i for i in range(1, len(languages)+1)]
print(languages, numbers)
result_list_with_tuples = []
for lang, num in zip(languages, numbers):
    print(lang, num)