# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки. 
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Итоговый список сохранить в виде json-объекта в соответствующий файл.

import json
profit = {}
profit_avg_dict = {}
summ_profit = 0
average_profit = 0
i = 0
with open('for_task_7.txt', 'r') as file:
    for line in file:
        name, firm, income, loss = line.split()
        profit[name] = int(income) - int(loss)
        if profit.setdefault(name) >= 0:
            summ_profit = summ_profit + profit.setdefault(name)
            i += 1
    if i != 0:
        average_profit = summ_profit / i
        print('Средняя прибыль: {:.2f}'.format(average_profit))
    else:
        print('Бизнеса нет, все забрали за долги')
    profit_avg_dict = {'average income': round(average_profit)}
    profit.update(profit_avg_dict)
    print('Прибыль каждой компании - {}'.format(profit))

with open('for_task_7_json.js', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'json-файл: \n '
          ' {}'.format(js_str))