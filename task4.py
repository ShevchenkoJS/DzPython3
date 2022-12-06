# Задача 4

print('Напишите программу, которая будет преобразовывать десятичное число в двоичное')

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input('Введите десятичное число: '))
result = ''
while number > 0:
    result += str(number % 2)
    number //= 2

print(result[::-1])  # или print(bin(number)[2:])