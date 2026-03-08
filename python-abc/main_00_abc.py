#!/usr/bin/env python3
from task_00_abc import Animal, Dog, Cat

bobby = Dog()
garfield = Cat()
print(bobby.sound())
print(garfield.sound())

try:
    animal = Animal()
    print(animal.sound())
except TypeError as e:
    print(e)
