"""
Есть класс "Воин". От него создаются два экземпляра-юнита. 
Каждому устанавливается здоровье в 100 очков. В случайном порядке они бьют друг друга. 
Тот, кто бьет, здоровья не теряет. У того, кого бьют, 
оно уменьшается на 20 очков от одного удара. 
После каждого удара надо выводить сообщение, 
какой юнит атаковал, и сколько у противника осталось здоровья. 
Как только у кого-то заканчивается ресурс здоровья, 
программа завершается сообщением о том, кто одержал победу.
"""

from random import random
class Solder:
    health = 100

unit_1 = Solder()
unit_2 = Solder()

while unit_1.health > 0 and unit_2.health > 0:
    a1 = random()
    a2 = random()
    if a1 > a2:
        unit_1.health -= 20
        print ("Атаковал Воин_2, здоровье Воин_1:", unit_1.health)
    else:
        unit_2.health -= 20
        print ("Атаковал Воин_1, здоровье Воин_2:", unit_2.health)

if unit_1.health > 0:
    print ("Победу одержал Воин_1")
else: 
    print ("Победу одержал Воин_2")