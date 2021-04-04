# ЛОТО
import random 

def backpack():
    return random.sample(range(1,91),90)

def player():
    return random.sample(range(1,91),15)

def row(values):
    values.sort()

    spaces_list = random.sample(range(8),4)
    spaces_list.sort()

    j = 0
    k = 0
    row = []

    for i in range(0,9):
        try:
            if i == spaces_list[j]:
                row.append(' ')
                j += 1
            else:
                row.append(values[k])
                k += 1

        except IndexError:
            row.append(values[k])
            k += 1
    return row

def victory(user,computer,items,gamer_1,gamer_2):
    if len(gamer_1) == 0:
        return print('Вы победили!')
    elif len(gamer_2) == 0:
        return print('Победил компьютер')
    elif len(gamer_1) == 0 and len(gamer_2) == 0:
        return print('Ничья')
    else:
        return display(user,computer,items,gamer_1,gamer_2)

def display(user,computer,items,gamer_1,gamer_2):
    print('\n')
    print('Новый бочонок: ', items[0])
    print('---- Ваша карточка ----')
    j = 0
    for i in range(len(user)):
        print(user[i][j],user[i][j+1],user[i][j+2],user[i][j+3],user[i][j+4],user[i][j+5],user[i][j+6],user[i][j+7],user[i][j+8])

    print('--------------------------')

    print('-- Карточка компьютера --')
    j = 0
    for i in range(len(computer)):
        print(computer[i][j],computer[i][j+1],computer[i][j+2],computer[i][j+3],computer[i][j+4],computer[i][j+5],computer[i][j+6],computer[i][j+7],computer[i][j+8])

    for i in range(len(computer)):
        for j in range(len(computer[i])):
            if computer[i][j] == items[0]:
                computer[i][j] = '-'
                gamer_2 = gamer_2[1:]
    
    decision(user,computer,items,gamer_1,gamer_2)
    

def decision(user,computer,items,gamer_1,gamer_2):
    choice = str(input('Зачеркнуть цифру? (y for "Yes", another key for "No", q for "Quit")'))
    while choice != 'q':
        if choice == 'y':
            print('yes')
            for i in range(len(user)):
                for j in range(len(user[i])):
                    if user[i][j] == items[0]:
                        user[i][j] = '-'
                        items = items[1:]
                        gamer_1 = gamer_1[1:]
                        return victory(user,computer,items,gamer_1,gamer_2)
                    elif user[i][j] != items[0] and user[i][j] == user[len(user)-1][len(user[i])-1]:
                        return print('Вы проиграли')

        elif choice != 'y':
            print('no')
            for i in range(len(user)):
                for j in range(len(user[i])):
                    if user[i][j] == items[0]:
                        return print('Вы проиграли')
                    elif user[i][j] == user[len(user)-1][len(user[i])-1] and user[i][j] != items[0]:
                        items = items[1:]
                        return victory(user,computer,items,gamer_1,gamer_2)
    else:
        return print('\n Вы прервали игру')


gamer_1 = player()
gamer_2 = player()
items = backpack()

user = [row(gamer_1[5*0:5*1]),row(gamer_1[5*1:5*2]),row(gamer_1[5*2:5*3])]
computer = [row(gamer_2[5*0:5*1]),row(gamer_2[5*1:5*2]),row(gamer_2[5*2:5*3])]

display(user,computer,items,gamer_1,gamer_2)