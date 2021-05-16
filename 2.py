# 2 .Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


name = str(input("Введите Имя"))
surname = str(input("Введите Фамилию"))
year = str(input("Введите Год"))
city = str(input("Введите Город"))
email = str(input("Введите email"))
phone = str(input("Введите Телефон"))

def my_func (name, surname, year, city, email, phone):
     return ' '.join([name, surname, year, city, email, phone])
print(my_func(name, surname, year, city, email, phone))
