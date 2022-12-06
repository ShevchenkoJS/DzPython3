# Задача 3

print('Задайте список из вещественных чисел. Напишите программу,')
print('которая найдёт разницу между максимальным и минимальным значением дробной части элементов')

# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19 
# (максимальное значение у числа 1.2 , минимальное у 10.01)

def separate_fraction(num: float) -> float:
    """Отделяет дробную часть от целой"""
    list_num = str(num).split('.') #['1','11']
    return float('0.'+list_num[1]) #[0.11]

def max_vs_min_fraction(num_list: list[float]) -> float:
    """Возвращает разницу между максимальным и минимальным дробным значением списка"""
    new_list = [separate_fraction(i)for i in num_list if int(i) != float(i)]
    print(new_list)
    return max(new_list) - min(new_list)

example = [1.1, 1.2, 3.1, 5, 10.01]
print(max_vs_min_fraction(example))