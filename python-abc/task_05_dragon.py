#!/usr/bin/python3
"""module that defines mixins and Dragon Class"""


class SwimMixin:
    def swim(self):
        print("The creature swims!")
  

class FlyMixin:
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")

class draco(Dragon):
    print(FlyMixin, SwimMixin, Dragon.roar)