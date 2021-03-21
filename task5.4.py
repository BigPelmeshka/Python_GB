# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

dictionary = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}


with open('for_task_4_input.txt', 'r', encoding='utf-8') as file_read:
    lines = file_read.readlines()

with open('for_task_4_output.txt', 'a', encoding='utf-8') as file_write:
    for line in lines:
        row = line.split()
        row[0] = dictionary[row[0]]
        print(' '.join(row), file=file_write)