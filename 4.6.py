# Реализовать два небольших скрипта:
#а) итератор, генерирующий целые числа, начиная с указанного,
#б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import count

for i in count(int(input('Beginning '))):
    if i > 20:
        break
    else: 
        print(i)

from itertools import cycle

_list_ = [False, None, 1, 'GeekBrains']
count = 0
for item in cycle(_list_):
    if count > 7:
        break
    print(item)
    count += 1