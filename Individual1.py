#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 7. Создать класс Date для работы с датами в формате «год.месяц.день». Дата представляется
# структурой с тремя полями типа unsigned int: для года, месяца и дня. Класс должен
# включать не менее трех функций инициализации: числами, строкой вида «год.месяц.день»
# (например, «2004.08.31») и датой. Обязательными операциями являются: вычисление даты
# через заданное количество дней, вычитание заданного количества дней из даты,
# определение високосности года, присвоение и получение отдельных частей (год, месяц,
# день), сравнение дат (равно, до, после), вычисление количества дней между датами.

import datetime


class Date:

    def __init__(self, year=1, month=1, day=1, days=10):
        self.year = int(year)
        self.month = int(month)
        self.day = int(day)
        self.days = float(days)

    def lt(self):
        a = datetime.date(self.year, self.month, self.day)
        b = datetime.timedelta(days=self.days)
        return f"После: {a + b < a - b}"

    def eq(self):
        a = datetime.date(self.year, self.month, self.day)
        b = datetime.timedelta(days=self.days)
        return f"Равно: {a + b == a - b}"

    def gt(self):
        a = datetime.date(self.year, self.month, self.day)
        b = datetime.timedelta(days=self.days)
        return f"До: {a + b > a - b}"

    def difference(self):
        a = datetime.date(self.year, self.month, self.day)
        b = datetime.timedelta(days=self.days)
        x = a + b
        y = a - b
        return f"Кол-во дней между датами: {x - y}"

    def __str__(self):
        leap = (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)
        return f"{self.year, self.month, self.day} \nВисокосный: {leap}"

    def __lt__(self, other):
        return (self.year, self.month, self.day) < (other.year, other.month, other.day)

    def __gt__(self, other):
        return (self.year, self.month, self.day) > (other.year, other.month, other.day)

    def __eq__(self, other):
        return (self.year, self.month, self.day) == (other.year, other.month, other.day)

    def __ge__(self, other):
        return (self.year, self.month, self.day) >= (other.year, other.month, other.day)

    def __le__(self, other):
        return (self.year, self.month, self.day) <= (other.year, other.month, other.day)


if __name__ == '__main__':
    r1 = Date(year=2020, month=1, day=24)
    print(f"r1 = {r1}")
    r2 = Date(year=1999, month=3, day=20)
    print(f"r2 = {r2}")
    print(r1.difference())
    print(r1.lt())
    print(r1.eq())
    print(r1.gt())

    print(f"r1 < r2: {r1 < r2}")
    print(f"r1 > r2: {r1 > r2}")
    print(f"r1 == r2: {r1 == r2}")
    print(f"r1 >= r2: {r1 >= r2}")
    print(f"r1 <= r2: {r1 <= r2}")
