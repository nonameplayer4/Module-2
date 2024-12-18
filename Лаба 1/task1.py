# TODO Написать 3 класса с документацией и аннотацией типов
class Knight:
    '''
    Документация на класс
    Класс описывает характеристики отважного рыцаря
    '''
    '''
    Example:
    >>> knight = Knight(40, 50, 60)
    >>> knight.method_1()
    >>> knight.method_2()
    >>> knight = Knight(40, '20', 60,5)
    Traceback (most recent call last):
      File "/private/var/folders/v4/tb1t2lr562zg4rqmyp2btv4c0000gn/T/AppTranslocation/6645EDC8-26D6-412E-B645-23FFF9239100/d/PyCharm CE.app/Contents/plugins/python-ce/helpers/pydev/pydevconsole.py", line 364, in runcode
        coro = func()
      File "<input>", line 1, in <module>
    TypeError: __init__() takes 4 positional arguments but 5 were given


    '''

    def __init__(self, speed: int, health: int, power: int):
        ''' Валидация и инициализация атрибутов '''
        if not isinstance(speed, int):
            raise TypeError
        if not (0 <= speed <= 100):
            raise ValueError
        self.speed = speed

        if not isinstance(health, int):
            raise TypeError
        if not (0 <= health <= 100):
            raise ValueError
        self.health = health

        if not isinstance(power, int):
            raise TypeError
        if not (0 <= power <= 100):
            raise ValueError
        self.power = power

    def method_1(self):
        # Даём имя рыцарю
        ...

    def method_2(self):
        # Выбираем цвет плащя рыцаря
        ...


class Floor:
    '''
    Документация на класс
    Класс описывает параметры пола в квартире
    '''
    '''
    Example:
    >>> floor = Floor('linoleum', 50)
    >>> floor.method_1()
    >>> floor.method_2()
    >>> floor = Floor('плитка', 11,1)
    Traceback (most recent call last):
      File "/private/var/folders/v4/tb1t2lr562zg4rqmyp2btv4c0000gn/T/AppTranslocation/6645EDC8-26D6-412E-B645-23FFF9239100/d/PyCharm CE.app/Contents/plugins/python-ce/helpers/pydev/pydevconsole.py", line 364, in runcode
        coro = func()
      File "<input>", line 1, in <module>
    TypeError: __init__() takes 3 positional arguments but 4 were given'''

    def __init__(self, floor_type: str, area: [int, float]):
        ''' Валидация и инициализация атрибутов '''
        if not isinstance(floor_type, str):
            raise TypeError
        if not floor_type.lower() in ['linoleum', 'tile', 'parquet']:
            raise ValueError
        self.floor_type = floor_type

        if not isinstance(area, (int, float)):
            raise TypeError
        if area < 0:
            raise ValueError
        self.area = area

    def method_1(self):
        # Рассчитываем стоимость покрытия пола (в зависимости от материала и площади)
        ...

    def method_2(self):
        # Рассчитываем общий вес пола (в зависимости от материала и площади)
        ...


class Marmalade:
    '''
    Документация на класс
    Класс описывает возможные сортировки мармеладок
    различных вкусов в магазине
    '''
    '''
    Example:
    >>> marmalade = Marmalade(22.1, 22.4, 25.01)
    >>> marmalade.method_1()
    >>> marmalade = Marmalade(22, 11, 42)
    Traceback (most recent call last):
      File "/private/var/folders/v4/tb1t2lr562zg4rqmyp2btv4c0000gn/T/AppTranslocation/6645EDC8-26D6-412E-B645-23FFF9239100/d/PyCharm CE.app/Contents/plugins/python-ce/helpers/pydev/pydevconsole.py", line 364, in runcode
        coro = func()
      File "<input>", line 1, in <module>
      File "<input>", line 72, in __init__
    TypeError
'''

    def __init__(self, strawberry: float, raspberry: float, cherry: float):
        ''' Валидация и инициализация атрибутов '''
        if not isinstance(strawberry, float):
            raise TypeError
        self.strawberry = strawberry

        if not isinstance(raspberry, float):
            raise TypeError
        self.raspberry = raspberry

        if not isinstance(cherry, float):
            raise TypeError
        self.cherry = cherry

    def method_1(self):
        # Фасуем мармеладки, если больше всего вишнёвых
        ...

    def method_2(self):
        # Фасуем мармеладки, если больше всего клубничных
        ...

    def method_3(self):
        # Фасуем мармеладки, если больше всего малиновых
        ...


if __name__ == "__main__":
    import doctest
    doctest.testmod()