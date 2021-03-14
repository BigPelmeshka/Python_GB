# Реализовать функцию, принимающую несколько параметров, 
# описывающих данные пользователя: имя, фамилия, год рождения, 
# город проживания, email, телефон. Функция должна принимать параметры 
# как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def user(name, surname, yearofbirth, city, email, phone):
    return ' '.join([name, surname, yearofbirth, city, email, phone])

name = str(input('Имя'))
surname = str(input('Фамилия'))
yearofbirth = str(input('Год рождения'))
city = str(input('Город'))
email = str(input('Емаил'))
phone = str(input('Телефон'))

print(user(name, surname, yearofbirth, city, email, phone))