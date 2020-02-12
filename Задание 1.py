def my_func (x, y):
    return x / y
x = float(input('Введите число'))
y = float(input('Введите число на которое поделить 1 число'))
if y ==0:
    print('На ноль делить нельзя')
else:
    print('Результат деления: ', my_func(x,y))