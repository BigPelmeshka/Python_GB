# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

income = float(input('Введите выручку: '))
loss = float(input('Введите издержки: '))

print('Ваша выручка: ', income)
print('Ваши издержки: ', loss)
print(' ')

if income > loss:
    print('Фирма отработала с прибылью. Ваша рентабельность,% :', income/loss*100)
    staff = int(input('Введите число работающих сотрудников: '))
    print('Прибыль на одного сотрудника: ', income/staff)
else:
    print('Фирма отработала с убытком')
    