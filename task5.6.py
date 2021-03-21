# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

dictionary_subject = {}
with open('for_task_6.txt', 'r', encoding='utf-8') as init_f:
    for line in init_f:
        subject, lecture, practice, lab = line.split()
        dictionary_subject[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету - \n {dictionary_subject}')