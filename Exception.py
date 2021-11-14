class BoardOutException(Exception):
    @staticmethod
    def __str__():
        return f'Ты пальнул за приделы поля'


class RepeatBordException(Exception):
    @staticmethod
    def __str__():
        return f'Здесь уже воронка. Выбери другую цель'
