#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
В следующих заданиях требуется реализовать абстрактный базовый класс, определив в нем абстрактные методы и свойства. Эти методы определяются в производных классах. 
В базовых классах должны быть объявлены абстрактные методы ввода/вывода, которые реализуются в производных классах. Вызывающая программа должна продемонстрировать 
все варианты вызова переопределенных абстрактных методов. Написать функцию вывода, получающую параметры базового класса по ссылке и демонстрирующую виртуальный вызов.
Создать абстрактный базовый класс Triangle для представления треугольника с виртуальными функциями вычисления площади и периметра. 
Поля данных должны включать две стороны и угол между ними. Определить классы-наследники: прямоугольный треугольник, равнобедренный треугольник, 
равносторонний треугольник со своими функциями вычисления площади и периметра.

"""

from abc import ABC, abstractmethod
from math import sqrt, pow


class Triangle(ABC):
    @abstractmethod
    def input_sides(self):
        pass


class Right_Triangle(Triangle):
    # переопределение абстрактного метода
    def input_sides(self):
        print("Прямоугольный треугольник:")
        a = float(input("Введите длину первого катета: "))
        b = float(input("Введите длину второго катета: "))
        return a, b

    def calculate_area(self, a, b):
        ar = a * b / 2
        print(f"Площадь: {ar:.2f}")

    def calculate_perimeter(self, a, b):
        c = sqrt(pow(a, 2) + pow(b, 2))
        per = a + b + c
        print(f"Периметр: {per:.2f}")


class Isosceles_Triangle(Triangle):
    # переопределение абстрактного метода
    def input_sides(self):
        print("Равнобедренный треугольник:")
        a = float(input("Введите длину боковых сторон: "))
        b = float(input("Введите длину основания: "))
        return a, b

    def calculate_area(self, a, b):
        h = sqrt(pow(a, 2) - pow(b, 2) / 4)
        ar = 1 / 2 * b * h
        print(f"Площадь: {ar:.2f}")

    def calculate_perimeter(self, a, b):
        per = 2 * a + b
        print(f"Периметр: {per:.2f}")


class Equilatreal_Triangle(Triangle):
    # переопределение абстрактного метода
    def input_sides(self):
        print("Равносторонний треугольник:")
        a = float(input("Введите длину сторон: "))
        return a

    def calculate_area(self, a):
        ar = (sqrt(3) * pow(a, 2)) / 4
        print(f"Площадь: {ar:.2f}")

    def calculate_perimeter(self, a):
        per = 3 * a
        print(f"Периметр: {per:.2f}")


if __name__ == "__main__":
    R = Right_Triangle()
    s = R.input_sides()
    R.calculate_area(*s)
    R.calculate_perimeter(*s)

    I = Isosceles_Triangle()
    s = I.input_sides()
    I.calculate_area(*s)
    I.calculate_perimeter(*s)

    E = Equilatreal_Triangle()
    s = E.input_sides()
    E.calculate_area(s)
    E.calculate_perimeter(s)
