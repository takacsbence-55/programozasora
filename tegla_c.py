import math


class Teglalap:
    def __init__(self, a=0, b=0, d=0):
        self.a = a
        self.b = b
        self.d = d

    def ter(self):
        return self.a*self.b

    def ker(self):
        return 2*(self.a+self.b)

    def kiir(self):
        print("A téglalap kerülete:",self.ker(),"A téglalap területe:",self.ter())

    def atlo(self):
        return round(math.sqrt(self.a**2+self.b**2),2)

    def sugar(self):
        return round(self.atlo()/2,2)

#+terület, kerület függvények és kör class