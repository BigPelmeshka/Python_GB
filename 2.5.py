# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.

list3 = [7, 5, 3, 3, 2]
print('Рейтинг - {}'.format(list3))
count = int(input('Введите общее количество чисел для формирования рейтинга: '))
j = 1
while j<=count: 
    digit = int(input('Введите число: '))
    for i in range(len(list3)):
        if list3[i] == digit:
            list3.insert(i + 1, digit)
            break
        elif list3[0] < digit:
            list3.insert(0, digit)
        elif list3[-1] > digit:
            list3.append(digit)
        elif list3[i] > digit and list3[i + 1] < digit:
            list3.insert(i + 1, digit)
    print('текущий список - {}'.format(list3))
    j += 1