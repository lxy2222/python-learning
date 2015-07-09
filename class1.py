
# -*- coding: utf-8 -*-

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

def run_twice(animal):
    animal.run()
    animal.run()

a = Animal()
d = Dog()
c = Cat()

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')
class Timer(object):
    def run(self):
        print('Start..')

t = Timer()
t.run()
run_twice(c)
run_twice(Tortoise())