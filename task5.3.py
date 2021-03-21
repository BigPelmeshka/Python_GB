# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

f = open('for_task_3.txt')

salaries = []
for worker in f:
  last_name, salary = worker.split()
  salary = int(salary)
  salaries.append(salary)
  if salary < 20000:
    print(last_name)

print('Средняя зарплата по отделу: ',sum(salaries)/len(salaries))
