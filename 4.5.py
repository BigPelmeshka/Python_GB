#Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.

from functools import reduce

def multiplying(a, b):
    return a * b

print('EVEN {}'.format([i for i in range(99, 1001) if i % 2 == 0]))
print('Перемножение {}'.format(reduce(multiplying, [i for i in range(99, 1001) if i % 2 == 0])))