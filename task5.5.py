# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('for_task_5.txt', 'w+') as file_:
    line = input('Input numbers with space delimiter \n')
    file_.writelines(line)
    numers = line.split()
    print(sum(map(float, numers)))
