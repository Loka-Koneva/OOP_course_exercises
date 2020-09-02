"""
Напишите программу по следующему описанию:
1) Есть класс Person, конструктор которого принимает три параметра (не учитывая self) – 
имя, фамилию и квалификацию специалиста. Квалификация имеет значение заданное по умолчанию, 
равное единице.
2) У класса Person есть метод, который возвращает строку, включающую в себя всю информацию о сотруднике.
3) Класс Person содержит деструктор, который выводит на экран фразу "До свидания, мистер …" 
(вместо троеточия должны выводиться имя и фамилия объекта).
4) В основной ветке программы создайте три объекта класса Person. 
Посмотрите информацию о сотрудниках и увольте самое слабое звено.
5) В конце программы добавьте функцию input(), чтобы скрипт не завершился сам, 
пока не будет нажат Enter. Иначе вы сразу увидите как удаляются все объекты при 
завершении работы программы.
"""

class Person:
    def __init__ (self, name, surname, qualification = 1):
        self.name = name
        self.surname = surname
        self.qualification = qualification
    def __del__(self):
        print ("До свидания, мистер ", self.name, self.surname)
    def getPerson(self):
        return "{0} {1}, {2}".format(self.name, self.surname, self.qualification)

person_1 = Person ("Иван", "Иванов", 5)
person_2 = Person ("Иван", "Петров", 10)
person_3 = Person ("Иван", "Сидоров")
print(person_1.getPerson())
print(person_2.getPerson())
print(person_3.getPerson())
del person_3
print ("Конец программы")
input ()