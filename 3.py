# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает
# сумму наибольших двух аргументов



def my_func(arg1, arg2, arg3):
    if arg1 > arg3 and arg2 > arg3:
        return arg1 + arg2
    elif arg2 < arg1 and arg2 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3


print(
    f'Резульат - {my_func(int(input("Первый аргумент ")), int(input("Второй аргумент ")), int(input("Третий аргумент ")))}')
