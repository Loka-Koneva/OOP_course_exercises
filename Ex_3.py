"""
В некой игре-стратегии есть солдаты и герои. 
У всех есть свойство, содержащее уникальный номер объекта, 
и свойство, в котором хранится принадлежность команде. 
У солдат есть метод "иду за героем", который в качестве аргумента принимает объект типа "герой". 
У героев есть метод увеличения собственного уровня.

В основной ветке программы создается по одному герою для каждой команды. 
В цикле генерируются объекты-солдаты. Их принадлежность команде определяется случайно. 
Солдаты разных команд добавляются в разные списки.

Измеряется длина списков солдат противоборствующих команд и выводится на экран. 
У героя, принадлежащего команде с более длинным списком, поднимается уровень.

Отправьте одного из солдат первого героя следовать за ним. 
Выведите на экран идентификационные номера этих двух юнитов.
"""

class Person:
    def __init__ (self, my_number, my_team=1):
        self.my_number = my_number
        self.my_team = my_team
    
class Hero(Person):
    def __init__ (self, my_number, my_team, my_level = 1):
        Person.__init__ (self, my_number, my_team)
        self.my_level = my_level
    def level (self):
        self.my_level +=1

class Soldier(Person):
    def follow_to_Hero(self, hero):
        self.hero = hero

hero_1 = Hero (1, 1)
hero_2 = Hero (2, 2)

team_1 = []
team_2 = []
