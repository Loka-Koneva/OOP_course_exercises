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
from random import randint

class Person:
    count = 0
    def __init__ (self, team):
        self.number = Person.count
        Person.count += 1
        self.team = team
    
class Hero(Person):
    def __init__ (self, team):
        Person.__init__ (self, team)
        self.level = 1
    def upLevel (self):
        self.level +=1

class Soldier(Person):
    def __init__ (self, team):
        Person.__init__(self, team)
        self.my_hero = None
    def follow_to_Hero(self, hero):
        self.my_hero = hero.number

hero_1 = Hero(1)
hero_2 = Hero(2)

team_1 = []
team_2 = []

for i in range (20):
    n = randint(1, 2)
    if n==1:
        team_1.append(Soldier(n))
    else:
        team_2.append(Soldier(n))

print(len(team_1), len(team_2))

if len(team_1)>len(team_2):
    hero_1.upLevel()
else:
    hero_2.upLevel()

team_1[0].follow_to_Hero(hero_1)
print(team_1[0].number, hero_1.number)

print ("Test commit")