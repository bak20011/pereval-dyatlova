# class Student:
#     course = 'Data Scientiest'
#
# s1 = Student()
#
# setattr(s1, "name","Иван")
# setattr(s1, "surname", "иванов")
# setattr(s1, "semestr", "1")
#
# result= s1.__dict__
# print(result)
import math


# class Person:
#     def __init__(self, name = None, age = None, gender = None, occupation = None ):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.occupation = occupation
#
#     def set_attributes(self,data):
#         for key, value in data.items():
#             setattr(self, key, value)
#
#     def show_card(self):
#         print(f"Name:{self.name} \nAge: {self.age}
#         \nGender: {self.gender} \nOccupation: {self.occupation}")
# class Queue:
#     def __init__(self):
#         self.items = []
#
#     def enqueue(self, item):
#         self.items.append(item)
#
#     def is_empty(self):
#         return len(self.items) == 0
#
#     def dequeue(self):
#         return self.items.pop(0)
#
#     def show_queue(self):
#         print(self.items)

# class User:
#     def __init__(self, email, password, balance):
#         self.email = email
#         self.password = password
#         self.balance = balance#
#     def login(self, email, password):
#         return self.email == email and self.password == password
#
#     def update_balance(self, amount):
#         self.balance += amount

class IntDataFrame:
    def __init__(self, column):
        self.column = [int(num) for num in column]

    def count(self, ):
        return len([num for num in self.column if num != 0])

    def unique(self):
        return len(set(self.column))


df = IntDataFrame([4.7, 4, 3, 0, 2.4, 0.3, 4])

print(df.column)
# [4, 4, 3, 0, 2, 0, 4]

print(df.count())
# 5

print(df.unique())
