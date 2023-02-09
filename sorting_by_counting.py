def sort_array(arr: list, max_item: int) -> list:
    array_ascii = [0] * (max_item + 1)
    result = []
    for i in arr:
        array_ascii[ord(i)] += 1
    # array_ascii - это массив в котором индекс элемента соответствует коду символа по системе ASCII
    for _, i in enumerate(array_ascii):
        if i != 0:
            while i > 0:
                result.append(chr(_))
                i -= 1
    return result


# array_input = ['a', 'n', 'a', 'a', 'e', 'a', 'p', 'd', 'x', '2']
array_input = list(input("Введите список: ").split(" "))
max_symbol = ord(max(array_input))
print(sort_array(array_input, max_symbol))

# Отсортировать этот массив с заданной сложностью можно с помощью метода сортировки подсчетом.
# Для сортировки буду использовать код символа в системе ASCll.
# 1. Нахожу максимальное значение в массиве и передаю его код в системе ASCII в функцию сортировки вместе с массивом.
# 2. В функции создаю два массива:
# - первый состоит из нулей, длинной равной максимальному значению переданному в функцию плюс единица;
# - второй пустой.
# 3. Итерирую сортируемый список для определения количества каждого элемента, при этом на каждой итерации в список
# с нулями добавляю единицу к значению по индексу равному коду в системе ASCII.
# Получаю список в котором каждый индекс соответствует коду символа в системе ASCII, а его значение количеству
# этих элементов в сортируемом массиве.
# 4. Циклом прохожу по полученному списку с количеством элементов, если значение не равно 0, то добавляю в список
# первый символ при этом уменьшая значение по этому индексу на единицу.
# 5. Возвращаю отсортированный массив
#
# Стабильный вариант алгоритма подсчетом возможен, при этом нужно дополнительно сохранить индекс последнего найденного
# элемента и в результирующий массив добавлять с учетом этого значения.
