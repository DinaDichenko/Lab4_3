#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
В некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее уникальный номер объекта, и свойство, в котором хранится принадлежность команде. У солдат есть метод "иду за героем", 
который в качестве аргумента принимает объект типа "герой". У героев есть метод увеличения собственного уровня. В основной ветке программы создается по одному герою для каждой команды. 
В цикле генерируются объекты-солдаты. Их принадлежность команде определяется случайно. Солдаты разных команд добавляются в разные списки. Измеряется длина списков солдат противоборствующих команд 
и выводится на экран. У героя, принадлежащего команде с более длинным списком, увеличивается уровень. Отправьте одного из солдат первого героя следовать за ним. Выведите на экран идентификационные 
номера этих двух юнитов.
"""
import random


class People:
    """
    Класс, хранящий информацию о уникальном номере объекта и принадлежности к команде
    """

    def __init__(self, identificator, command):
        """
        Конструктор класса, принимает два параметра, валидирует их и сохраняет в поля
        """
        if not isinstance(identificator, int):
            raise TypeError("Значение идентификатора должно быть целым числом")

        self.identificator = identificator
        self.command = command

    def display(self):
        """
        Метод вывода на консоль результатов
        """
        print(f"Идентификатор: {self.identificator}, Команда: {self.people_command()}")

    def people_command(self):
        """
        Метод возвращает принадлежность к команде
        """
        return self.command


class Hero(People):
    """
    Дочерний класс People, добавляет метод увеличения собственного уровня
    """

    def __init__(self, identificator, command, level=1):
        """
        Конструктор класса "Герой", добавляет новое поле - уровень
        """
        super().__init__(identificator, command)
        self.__level = level

    def level(self):
        """
        Метод увеличения уровня героя
        """
        self.__level += 1
        print(f"Уровень героя '{self.command}' увеличен. Новый уровень: {self.__level}")


class Soldier(People):
    """
    Дочерний класс People, добавляет метод "иду за героем"
    """

    def go_hero(self, hero):
        """
        Метод "иду за героем", принимает объект типа Hero
        """
        print(f"Солдат {self.identificator} идет за героем '{hero.people_command()}'")


def soldiers_count(hero):
    """
    Функция для определения количества солдат у героя
    """
    if hero.people_command() == "Команда 1":
        return len(soldiers_command_1)
    elif hero.people_command() == "Команда 2":
        return len(soldiers_command_2)
    elif hero.people_command() == "Команда 3":
        return len(soldiers_command_3)


if __name__ == "__main__":
    # Создаем три героя для каждой команды
    hero1 = Hero(1, "Команда 1")
    hero2 = Hero(2, "Команда 2")
    hero3 = Hero(3, "Команда 3")

    # Списки солдат для каждой команды
    soldiers_command_1 = []
    soldiers_command_2 = []
    soldiers_command_3 = []

    # Генерация солдат
    for hero in [hero1, hero2, hero3]:
        num_soldiers = random.randint(5, 15)  # случайное количество солдат от 5 до 15
        for i in range(num_soldiers):
            soldier = Soldier(i + 1, hero.people_command())
            if hero.people_command() == "Команда 1":
                soldiers_command_1.append(soldier)
            elif hero.people_command() == "Команда 2":
                soldiers_command_2.append(soldier)
            elif hero.people_command() == "Команда 3":
                soldiers_command_3.append(soldier)

    # Количество солдат у каждого героя
    print(f"Количество солдат команды 1: {len(soldiers_command_1)}")
    print(f"Количество солдат команды 2: {len(soldiers_command_2)}")
    print(f"Колитчество солдат команды 3: {len(soldiers_command_3)}")

    # Находим героя с большим количеством солдат и увеличиваем его уровень
    max_soldiers_hero = max([hero1, hero2, hero3], key=soldiers_count)
    max_soldiers_hero.level()

    # Выбираем случайного солдата первого героя и отправляем его следовать за героем
    random_soldier_hero1 = random.choice(soldiers_command_1)
    random_soldier_hero1.go_hero(hero1)
