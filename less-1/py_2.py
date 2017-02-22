
# TDD: разработка через тестирование

# Функция создает словарь из 2-х списков
def do_dict(lst1, lst2):
    '''
    Creates dict from 2 lists.

    >>> sorted(do_dict(['one', 'two', 'three'], [1, 2, 3]).items())
    [('one', 1), ('three', 3), ('two', 2)]

    # 1. добавить еще 2 примера для проверки
    # 2. проверить с помощью unittest
    '''
    d = {}
    for i, key in enumerate(lst1):
        value = lst2[i]
        d[key] = value
    return d



if __name__ == "__main__":
    import doctest
    doctest.testmod()
