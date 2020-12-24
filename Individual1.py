#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 7. Создать класс Date для работы с датами в формате «год.месяц.день». Дата представляется
# структурой с тремя полями типа unsigned int: для года, месяца и дня. Класс должен
# включать не менее трех функций инициализации: числами, строкой вида «год.месяц.день»
# (например, «2004.08.31») и датой. Обязательными операциями являются: вычисление даты
# через заданное количество дней, вычитание заданного количества дней из даты,
# определение високосности года, присвоение и получение отдельных частей (год, месяц,
# день), сравнение дат (равно, до, после), вычисление количества дней между датами.

# Выполнить индивидуальное задание 1 лабораторной работы 12, максимально задействовав
# имеющиеся в Python средства перегрузки операторов.

import datetime


class Date:

    def __init__(self, year=1, month=1, day=1, number=0, data1=0):
        self.year = int(year)
        self.month = int(month)
        self.day = int(day)
        self.number = float(number)
        self.data1 = int(data1)
        self.kk = 0
        self.cc = 0
        self.s = 0
        self.q = 0
        self.r = 0

        self.new_data()
        self.new_data1()
        self.leap_year()
        self.comparison()
        self.difference()

    def read(self):
        year = input("Введите год: ")
        month = input("Введите месяц: ")
        day = input("Введите день: ")
        number = input("Количество дней: ")

        self.year = int(year)
        self.month = int(month)
        self.day = int(day)
        self.number = int(number)

        self.new_data()
        self.new_data1()
        self.leap_year()
        self.comparison()
        self.difference()

    def display(self):
        print(f"{self.cc}")
        print(f"{self.kk}")
        print(f"{self.s}")
        print(f"{self.q}")
        print(f"{self.r}")

    def new_data(self):
        a = datetime.date(self.year, self.month, self.day)
        b = datetime.timedelta(days=self.number)
        self.cc = a + b

    def new_data1(self):
        a = datetime.date(self.year, self.month, self.day)
        b = datetime.timedelta(days=self.number)
        self.kk = a - b

    def leap_year(self):
        if (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):
            self.s = "Високосный"
        else:
            self.s = "Обычный"

    def comparison(self):
        if self.cc < self.kk:
            self.q = "После"
        if self.cc == self.kk:
            self.q = "Равно"
        else:
            self.q = "До"

    def difference(self):
        if self.cc > self.kk:
            self.r = self.cc - self.kk
        else:
            self.r = self.kk - self.cc

    def __lt__(self, other):
        return self.cc < other.cc

    def __gt__(self, other):
        return self.cc > other.cc

    def __le__(self, other):
        return self.cc <= other.cc

    def __ge__(self, other):
        return self.cc >= other.cc

    def __eq__(self, other):
        return self.cc == other.cc

    def __add__(self, other):
        return self.cc + other.cc

    def __sub__(self, other):
        return self.cc - other.cc


if __name__ == '__main__':
    r1 = Date()
    r1.read()
    r1.display()
    r2 = Date()
    r2.read()

    print(f"Year first < Year second?: {r1 < r2}")
    print(f"Year first > Year second?: {r1 > r2}")
    print(f"Year first <= Year second?: {r1 <= r2}")
    print(f"Year first >= Year second?: {r1 >= r2}")
    print(f"Year first = Year second?: {r1 == r2}")
    print(f"Year first + Year second?: {r1 + r2}")
    print(f"Year first - Year second?: {r1 - r2}")
