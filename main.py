# Подробнее о функциях
# объявим функцию, которая будет находить
# сумму всех чисел и длин всех строк
def calculate_structure_sum(*args):
# введем переменную s, которая будет считать эту сумму
# изначально для s присвоим значение ноль
    s = 0
    for name in args:
# если наш элемент - это число, то к
# сумме прибавляем сам элемент
        if isinstance(name, int):
            s += name
        elif isinstance(name, float):
            s += name
# если наш элемент строка, то к сумме
# прибавляем длину строки
        elif isinstance(name, str):
            s += len(name)
        elif isinstance(name, bool):
            s += name
# для списка или кортеза
        elif isinstance(name, (list, tuple)):
            s += calculate_structure_sum(*name)
# для множества
        elif isinstance(name, set):
            s += calculate_structure_sum(*name)
# для словаря
        elif isinstance(name, dict):
            keys = list(name.keys())
            values = list(name.values())
            for i in range(len(keys)):
                s = s + calculate_structure_sum(keys[i])
                s = s + calculate_structure_sum(values[i])
    return s


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
