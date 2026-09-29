from datetime import datetime
from time import sleep
from os import system
from os import name as os_name

def clear():
    """
    RU: Функция очистки стандартного потока вывода (терминала) через системные вызовы posix/nt.
    EN: Clears the standard output stream (terminal) using posix/nt system calls.
    """
    system("clear" if os_name == "posix" else "cls")


"""
RU: Пользовательский класс для инкапсуляции и валидации календарных дат (день, месяц, год).
EN: Custom class designed to encapsulate and validate calendar dates (day, month, year).
"""

class Date:

    """
    RU: Конструктор экземпляра класса. Защищает атрибуты от отрицательных значений с помощью условных операторов.
    EN: Class instance constructor. Protects attributes from negative values using conditional statements.
    """
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

        if self.year < 0:
            self.year = 0

        if self.month < 0:
            self.month = 0

        if self.day < 0:
            self.day = 0


    """
    RU: Проверяет равенство двух объектов Date на основе совпадения дня, месяца и года.
    EN: Checks equality of two Date objects based on the matching day, month, and year.
    """
    def __eq__(self, other):
        if not isinstance(other, Date):
            return False
        return self.day == other.day and self.month == other.month and self.year == other.year

    """
    RU: Покомпонентно складывает два объекта Date и возвращает новый объект даты.
    EN: Component-wise adds two Date objects and returns a new date object.
    """
    def __add__(self, other):
        if not isinstance(other, Date):
            return NotImplemented
        day = self.day + other.day
        month = self.month + other.month
        year = self.year + other.year
        return Date(day, month, year)

    """
    RU: Покомпонентно вычитает один объект Date из другого и возвращает новый объект даты.
    EN: Component-wise subtracts one Date object from another and returns a new date object.
    """
    def __sub__(self, other):
        if not isinstance(other, Date):
            return NotImplemented
        day = self.day - other.day
        month = self.month - other.month
        year = self.year - other.year
        return Date(day, month, year)

    """
    RU: Проверяет, является ли текущая дата строго меньшей (более ранней), чем другая.
    EN: Checks if the current date is strictly less than (earlier than) the other one.
    """
    def __lt__(self, other):
        if not isinstance(other, Date):
            return NotImplemented
        return (self.year, self.month, self.day) < (other.year, other.month, other.day)

    """
    RU: Проверяет, является ли текущая дата строго большей (более поздней), чем другая.
    EN: Checks if the current date is strictly greater than (later than) the other one.
    """
    def __gt__(self, other):
        if not isinstance(other, Date):
            return NotImplemented
        return (self.year, self.month, self.day) > (other.year, other.month, other.day)

    """
    RU: Проверяет, является ли текущая дата меньшей или равной другой дате.
    EN: Checks if the current date is less than or equal to the other one.
    """
    def __le__(self, other):
        if not isinstance(other, Date):
            return NotImplemented
        return (self.year, self.month, self.day) <= (other.year, other.month, other.day)

    """
    RU: Проверяет, является ли текущая дата большей или равной другой дате.
    EN: Checks if the current date is greater than or equal to the other one.
    """
    def __ge__(self, other):
        if not isinstance(other, Date):
            return NotImplemented
        return (self.year, self.month, self.day) >= (other.year, other.month, other.day)

    """
    RU: Возвращает понятное пользователю строковое представление даты в формате ДД/ММ/ГГГГ.
    EN: Returns a user-friendly string representation of the date in DD/MM/YYYY format.
    """
    def __str__(self):
        return f"{self.day:02d}/{self.month:02d}/{self.year:02d}"


class WatchTime:
    """
    RU: Пользовательский класс (тип данных) для инкапсуляции времени в 24-часовом формате.
    EN: Custom class (data type) designed to encapsulate time in a 24-hour format.
    """
    def __init__(self, hour, minute):
        """
        RU: Конструктор (инициализатор) экземпляра класса. Вычисляет переполнение минут через целочисленное деление и остаток от деления.
        EN: Class instance constructor (initializer). Calculates minute overflow using floor division and modulo operations.
        """
        self.hour = (hour + (minute // 60)) % 24
        self.minute = minute % 60

    def __eq__(self, other):
        """
        RU: Dunder-метод перегрузки оператора равенства (==). Проверяет соответствие типов через isinstance перед сравнением атрибутов.
        EN: Dunder method for overloading the equality operator (==). Validates types via isinstance before attribute comparison.
        """
        if not isinstance(other, WatchTime):
            return False
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, other):
        """
        RU: Dunder-метод перегрузки оператора сложения (+). Возвращает новый экземпляр класса или NotImplemented при несоответствии типов.
        EN: Dunder method for overloading the addition operator (+). Returns a new class instance or NotImplemented if types mismatch.
        """
        if not isinstance(other, WatchTime):
            return NotImplemented
        return WatchTime(self.hour + other.hour, self.minute + other.minute)

    def __sub__(self, other):
        """
        RU: Dunder-метод перегрузки оператора вычитания (-). Преобразует состояние обоих объектов в минуты для предотвращения багов знака.
        EN: Dunder method for overloading the subtraction operator (-). Converts both object states to minutes to prevent sign bugs.
        """
        if not isinstance(other, WatchTime):
            return NotImplemented
        return WatchTime(0, (self.hour * 60 + self.minute) - (other.hour * 60 + other.minute))

    def __lt__(self, other):
        """
        RU: Dunder-метод сравнения «меньше» (<). Использует лексикографическое сравнение кортежей (tuple).
        EN: Dunder method for 'less than' (<) comparison. Utilizes lexicographical tuple comparison.
        """
        if not isinstance(other, WatchTime):
            return NotImplemented
        return (self.hour, self.minute) < (other.hour, other.minute)

    def __gt__(self, other):
        """
        RU: Dunder-метод сравнения «больше» (>). Использует лексикографическое сравнение кортежей (tuple).
        EN: Dunder method for 'greater than' (>) comparison. Utilizes lexicographical tuple comparison.
        """
        if not isinstance(other, WatchTime):
            return NotImplemented
        return (self.hour, self.minute) > (other.hour, other.minute)

    def __le__(self, other):
        """
        RU: Dunder-метод сравнения «меньше или равно» (<=).
        EN: Dunder method for 'less than or equal to' (<=) comparison.
        """
        if not isinstance(other, WatchTime):
            return NotImplemented
        return (self.hour, self.minute) <= (other.hour, other.minute)

    def __ge__(self, other):
        """
        RU: Dunder-метод сравнения «больше или равно» (>=).
        EN: Dunder method for 'greater than or equal to' (>=) comparison.
        """
        if not isinstance(other, WatchTime):
            return NotImplemented
        return (self.hour, self.minute) >= (other.hour, other.minute)

    def __str__(self):
        """
        RU: Dunder-метод строкового представления объекта. Возвращает строку, отформатированную по спецификации f-string со спецификатором :02d.
        EN: Dunder method for object string representation. Returns an f-string formatted with the :02d specifier.
        """
        return f"{self.hour:02d}:{self.minute:02d}"


def RealTimeWatchTime(hour=0, minute=0):
    """
    RU: Фабричная функция для инициализации объекта WatchTime на основе текущего вызова метода datetime.now() с аргументами смещения.
    EN: Factory function to initialize a Watchfrom watchtime import TimeZone

    print(TimeZone(2))Time object based on a datetime.now() method call with offset arguments.
    """
    now = datetime.now()
    return WatchTime(now.hour + hour, now.minute + minute)

def TimeZone(zone_hour=0, zone_minute=0):
    """
    RU: Функция-алиас для получения текущего времени в виде объекта WatchTime и указания часового пояса.
    EN: Alias function to get the current time as a WatchTime object and specify the timezone offset.
    """
    return RealTimeWatchTime(zone_hour, zone_minute)

def WithDateTime(dt):
    """
    RU: Функция-адаптер (конвертер) для парсинга атрибутов .hour и .minute из экземпляра встроенного класса datetime.
    EN: Adapter (converter) function designed to parse .hour and .minute attributes from a built-in datetime instance.
    """
    if not isinstance(dt, datetime):
        raise TypeError("dt must be a datetime instance")

    return WatchTime(dt.hour, dt.minute)

def TodayDate(day, month, year):
    """
    RU: Функция форматирования текущей даты. Вызывает метод .strftime() экземпляра datetime.
    EN: Current date formatting function. Invokes the .strftime() method on a datetime instance.
    """
    now = datetime.now()
    return Date(now.day + day, now.month + month, now.year + year)
def AtThatMoment(action, *args, **kwargs):
    """
    RU: Функция, реализующая бесконечный цикл со встроенной обработкой исключения KeyboardInterrupt для перехвата сигналов прерывания SIGINT (Ctrl+C).
        Принимает callback-функцию 'action' и распаковывает кортеж позиционных (*args) и словарь именованных (**kwargs) аргументов.
    EN: Function implementing an infinite loop with built-in KeyboardInterrupt exception handling to catch SIGINT signals (Ctrl+C).
        Accepts an 'action' callback function and unpacks positional (*args) and keyword (**kwargs) argument collections.
    """
    while True:
        try:
            clear()
            # Передача распакованных аргументов в callable-объект action
            # Passing unpacked arguments into the callable action object
            print(action(*args, **kwargs))
            sleep(1)
        except KeyboardInterrupt:
            # Блок обработки исключения прерывания процесса
            # Exception handling block for process interruption
            print("Execution process stopped!")
            break
