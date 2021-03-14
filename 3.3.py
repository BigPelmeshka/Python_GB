# Реализовать функцию my_func(), которая принимает три позиционных аргумента, 
# и возвращает сумму наибольших двух аргументов.

def my_func(a,b,c):
    arg1 = a+b
    arg2 = a+c
    arg3 = b+c 
    list = [arg1,arg2,arg3]
    maxsum = 0
    for i in range(len(list)):
        if list[i] >= maxsum:
            maxsum = list[i]
    
    return maxsum

my_func(1,11,23)