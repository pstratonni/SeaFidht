class BoardWrongShipException(Exception):
    pass


class BoardOutException(BoardWrongShipException):
    @staticmethod
    def __str__():
        return f'Ты пальнул за приделы поля'


class RepeatBordException(BoardWrongShipException):
    @staticmethod
    def __str__():
        return f'Здесь уже воронка. Выбери другую цель'

# class BowShipOutException(Exception):
#     @staticmethod
#     def __str__(self):
#         return f'Нос корабля на мели. Быстрей выбери другую точку'
#
#
# class ShipOutException(Exception):
#     @staticmethod
#     def __str__(self):
#         return f'Корабль слишком длинный (вышел за приделы поля, наехал на другой)'
