#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Составить программу с использованием иерархии классов. Номер варианта необходимо получить у преподавателя. В раздел программы, начинающийся после инструкции if __name__= '__main__': 
добавить код, демонстрирующий возможности разработанных классов. 
Создать класс Man (человек), с полями: имя, возраст, пол и вес. Определить методы переназначения имени, изменения возраста и изменения веса. Создать производный класс Student, 
имеющий поле года обучения. Определить методы переназначения и увеличения года обучения.

"""


class Man:
    """
    Класс, хранящий онформацию о людях
    """

    def __init__(self, name, age, sex, weight):
        """
        Конструктор класса
        """
        if (not isinstance(age, int)) and (age < 0):
            raise TypeError("Возраст должен быть целым положительным числом")

        if weight <= 0:
            raise TypeError("Вес должен быть положительным числом")

        self.name = name
        self.age = age
        self.sex = sex
        self.weight = weight

    def display(self):
        """
        Метод вывода на консоль результатов
        """
        print(
            f"Имя: {self.name}, Пол: {self.sex}, Возраст: {self.age}, Вес: {self.weight}"
        )

    def set_name(self, new_name):
        """
        Метод переназначения имени
        """
        self.name = new_name

    def set_age(self, new_age):
        """
        Метод изменения возраста
        """
        if (not isinstance(new_age, int)) and (new_age < 0):
            raise TypeError("Возраст должен быть целым положительным числом")

        self.age = new_age

    def set_weight(self, new_weigth):
        """
        Метод изменения веса
        """
        if new_weigth <= 0:
            raise TypeError("Вес должен быть положительным числом")

        self.weight = new_weigth


class Student(Man):
    """
    Дочерний класс Man
    """

    def __init__(self, name, age, sex, weight, year):
        """
        Конструктор класса "Герой", добавляет новое поле - уровень
        """
        super().__init__(name, age, sex, weight)
        self.__year = year

    def up_year(self):
        """
        Метод увеличения года обучения
        """
        self.__year += 1

    def set_year(self, new_year):
        """
        Метод переназначения года обучения
        """
        self.__year = new_year

    def display(self):
        """
        Метод вывода на консоль результатов
        """
        print(
            f"\nИмя: {self.name}, Пол: {self.sex}, Возраст: {self.age}, Вес: {self.weight}, Год обучения: {self.__year}"
        )


if __name__ == "__main__":
    people = Man("Дмитрий", 20, "Мужчина", 70)
    people.display()

    people.set_name("Дима")
    people.set_age(21)
    people.set_weight(67)
    people.display()

    student = Student("Алиса", 20, "Женщина", 55, 1)
    student.display()

    student.up_year()
    student.display()

    student.set_year(3)
    student.display()
