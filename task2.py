# Задача 2
print('Напишите программу, которая найдёт произведение пар чисел списка.')
print('Парой считаем первый и последний элемент, второй и предпоследний и т.д')

# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

nums = list()
for element in input('Введите числа через пробел: ').split():
    nums.append(int(element))

def pair_multi(nums: list[int]) -> list[int]:
    """Возвращает список произведений пар элементов"""
    pairs = []
    iterations = ((len(nums)+1)//2)
    print(iterations)
    for i in range(iterations):
        pairs.append(nums[i]*nums[-1-i])
    return pairs

print(pair_multi(nums))