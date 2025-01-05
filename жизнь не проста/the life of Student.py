# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def can_walk(self):
#         print(f"{self.name} can walk")


# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year

#     def display_info(self):
#         print(f"{self.title}, {self.author}, {self.year}")


                                        #1
# class Student:
#  print("Hi")

#  def __init__(self):
#     self.height = 160
#     print("I am alive!")

# first_student = Student()
                                    # 2
# class Student:
#     def __init__(self):
#         self.rost = 171

# Mike = Student()
# print(f"Рост Майка - {Mike.rost}")
                                        # 3
# class Student:
#     def __init__(self, rost = 160):
#         self.rost = rost

# nick = Student()
# kate = Student(rost = 170)
# print(f"Рост nick - {nick.rost}")
# print(f"Рост kate - {kate.rost}")

#                       Самостоятельная работа
# class Shkolnik:
#     def __init__(self, rost, old, name):
#         self.rost = rost
#         self.old = old
#         self.name = name
#     def display_info(self):
#         print(f"{self.rost}", "{self.old}", "{self.name}")
        
    
# Shkolnik1 = Shkolnik(182, 16, "Mickle")
# print(f"Рост - {Shkolnik1.rost}")
# print(f"Лет - {Shkolnik1.old}")
# print(f"Имя - {Shkolnik1.name}")

# print("==============================")        
# Shkolnik2 = Shkolnik(162, 15, "Anna")
# print(f"Рост - {Shkolnik2.rost}")
# print(f"Лет - {Shkolnik2.old}")
# print(f"Имя - {Shkolnik2.name}")


#                                           Симулятор студента, то есть выводит сколько всего студентов я объявил
# class Student:
#     amount_of_students = 0
#     def __init__(self, height=160):
#         self.height = height
#         Student.amount_of_students += 1

# Alice = Student()
# nick = Student()
# kate = Student(height=170)
# print(nick.amount_of_students)
# print(Student.amount_of_students)

#                           если реально, то я не совсем не понял код от ITstep :(
# class Student:
#     amount_of_students = 0
#     def __init__(self, height=160):
#         self.height = height
#         Student.amount_of_students += 1
#     def grow(self, height=1):
#         self.height += height

# nick = Student()
# kate = Student(height=170)
# nick.grow(height=15)
# print(kate.height)
# print(nick.height)

#                                           фишка которую можно использовать                                                  
# class Student:
#     def __init__(self, name = None, age = None):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"I am a student. My name is {self.name}, and i'm old {self.age}."

# nick = Student(name = "Nick", age = 23)
# print(nick)

#                               __del__
# class Student:
#     def __init__(self, name=None):
#         self.name = name
#     def __del__(self):
#         print("Training is over. I am now an expert!")

# nick = Student()

import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
    def to_study(self):
        pass
    def to_sleep(self):
        pass
    def to_chill(self):
        pass
    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression...")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally...")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
    def live(self):
        pass
    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life "
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()

nick = Student(name="Nurdaulet")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)

