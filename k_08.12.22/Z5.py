# 5. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.\
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# 12A11B10C6D5E4FG python is s7o c7ol

def coding(txt):
    count = 1
    sign = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            sign = sign + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        sign = sign + str(count) + txt[-1]
    return sign

def decoding(txt):
    number = ''
    sign = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            sign = sign + txt[i] * int(number)
            number = ''
    return sign


s = input("Введите текст: ")
print(f"Текст после шифровки: {coding(s)}")
print(f"Текст после дешифровки: {decoding(coding(s))}")