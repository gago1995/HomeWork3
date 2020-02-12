mylist = []
summa = 0
while True:
    mylist.extend(map(int,input('Введите числа через пробел').split()))
    summa = sum(mylist)
    print(f'Сумма: {summa}')
    if input('Выход - N, \nЛюбая клавиша - продолжить: ').upper() == 'N':
        break
    else:
        continue
print(f'Сумма: {summa}')